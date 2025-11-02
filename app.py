import os
from datetime import datetime

from flask import Flask, Response, render_template, request
from flask_cors import CORS

import db

app = Flask(__name__)

db.create_table()
CORS(app, origins=os.getenv("NEOCITIES_ORIGIN", "*"))


@app.route("/count-up/<path:page_name>")
def neocities_count_up(page_name):
    log = {
        "page_name": page_name,
        "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "remote_addr": request.remote_addr,
        "user_agent": request.user_agent.string,
        "languages": request.headers.get("Accept-Language"),
        "referrer": request.referrer,
    }
    print(log)
    db.count_up(log)

    return Response("", mimetype="application/javascript")


@app.route("/count-view")
def neocities_count_view():
    logs = db.count_view()
    return render_template("counter-view.html", logs=logs)
