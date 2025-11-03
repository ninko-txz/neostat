import os
from datetime import datetime, timedelta, timezone

from flask import Flask, Response, render_template, request
from flask_cors import CORS
from geoip2 import database as geoip
from geoip2.errors import AddressNotFoundError

import db

app = Flask(__name__)

db.create_table()

AUTH_USERNAME = os.getenv("NEOSTAT_USERNAME", "admin")
AUTH_PASSWORD = os.getenv("NEOSTAT_PASSWORD", "password")
AUTH_TOKEN = os.getenv("NEOSTAT_TOKEN", "neostat")
CORS(app, origins=os.getenv("NEOSTAT_CORS", "*"))


@app.route("/<path:page_name>/neostat.js")
def neostat_count_up(page_name):
    if request.cookies.get("neostat-auth-token") != AUTH_TOKEN:
        count_up(page_name, request)

    response = Response('"use strict";', mimetype="application/javascript")
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True

    return response


@app.route("/neostat")
def neostat():
    auth = request.authorization

    if auth is None:
        response = Response("Login Required", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})
        return response

    if auth.username == AUTH_USERNAME and auth.password == AUTH_PASSWORD:
        response = Response(render_template("neostat.html", logs=db.count_view()))
        response.set_cookie("neostat-auth-token", AUTH_TOKEN, max_age=60 * 60 * 24 * 365 * 10)
        return response

    else:
        response = Response("Login Failed", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})
        return response


def count_up(page_name, request):
    x_forwarded = request.headers.get("X-Forwarded-For")

    log = {
        "created_at": now(),
        "page_name": page_name,
        "x_forwarded": x_forwarded,
        "country": None if x_forwarded is None else get_country(x_forwarded),
        "user_agent": request.user_agent.string,
        "languages": request.headers.get("Accept-Language"),
        "referrer": request.referrer,
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
