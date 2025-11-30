import os
from datetime import datetime, timedelta, timezone

from flask import Flask, Response, render_template, request
from flask_cors import CORS
from geoip2 import database as geoip
from geoip2.errors import AddressNotFoundError

import db

AUTH_USERNAME = os.getenv("NEOSTAT_USERNAME", "admin")
AUTH_PASSWORD = os.getenv("NEOSTAT_PASSWORD", "password")
AUTH_TOKEN = os.getenv("NEOSTAT_TOKEN", "neostat")

GEOLOCATION = os.getenv("NEOSTAT_GEOLOCATION") is not None
REFERRER = ORIGIN = os.getenv("NEOSTAT_ORIGIN")

db.create_table()

app = Flask(__name__)

# CORS制限有効化
CORS(app, origins=ORIGIN)


@app.route("/beacon/<path:url_path>.js")
def neostat_count_up(url_path):
    if includes("ignore_ua.txt", request.user_agent.string):
        return build_response()

    if request.referrer != REFERRER:
        return build_response()

    if request.cookies.get("neostat-auth-token") == AUTH_TOKEN:
        return build_response()

    count_up(url_path, request)

    return build_response()


@app.route("/admin")
def neostat():
    auth = request.authorization

    if auth is None:
        response = Response("Login Required", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})
        return response

    if auth.username == AUTH_USERNAME and auth.password == AUTH_PASSWORD:
        response = Response(render_template("neostat.html", logs=db.count_view()))
        response.set_cookie(
            "neostat-auth-token", AUTH_TOKEN, max_age=60 * 60 * 24 * 365 * 10, samesite="None", secure=True
        )
        return response

    else:
        response = Response("Login Failed", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})
        return response


def count_up(url_path, request):
    x_forwarded = request.headers.get("X-Forwarded-For")

    log = {
        "created_at": now(),
        "path": url_path,
        "x_forwarded": x_forwarded,
        "country": None if x_forwarded is None else get_country(x_forwarded),
        "user_agent": request.user_agent.string,
        "languages": request.headers.get("Accept-Language"),
    }

    db.count_up(log)


def get_country(ip):
    try:
        reader = geoip.Reader("./geolite.mmdb")
        return reader.country(ip).country.names["en"]

    except AddressNotFoundError:
        return None


def now():
    utc_now = datetime.now(timezone.utc)
    jst_now = utc_now + timedelta(hours=9)
    return jst_now.strftime("%Y-%m-%d %H:%M:%S")


def includes(file, string):
    with open(file, "r") as f:
        for line in f:
            if line == string:
                return True
        return False


def build_response():
    response = Response('"use strict";', mimetype="application/javascript")

    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True

    return response
