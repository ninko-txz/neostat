import os
from datetime import datetime, timedelta, timezone

from flask import Flask, Response, render_template, request
from flask_cors import CORS
from geoip2 import database as geoip
from geoip2.errors import AddressNotFoundError

import db

app = Flask(__name__)

db.create_table()
CORS(app, origins=os.getenv("NEOCITIES_ORIGIN", "*"))


@app.route("/<path:page_name>/neostat.js")
def neocities_count_up(page_name):
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

    return Response('"use strict";', mimetype="application/javascript")


@app.route("/neostat")
def neocities_count_view():
    logs = db.count_view()
    return render_template("neostat.html", logs=logs)


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
