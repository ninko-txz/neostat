import time

from flask import Flask, Response, render_template_string, request

import db
import settings
import template

app = Flask(__name__)


@app.route("/beacon/<path:path>.js")
def beacon(path):
    if request.user_agent in settings.IGNORE_USER_AGENTS:
        return empty_js()

    if request.referrer != settings.ALLOWED_REFERRER:
        return empty_js()

    if request.cookies.get(settings.COOKIE_NAME) == settings.COOKIE_VALUE:
        return empty_js()

    created_at = int(time.time())
    x_forwarded = request.headers.get("X-Forwarded-For")
    user_agent = request.user_agent.string
    languages = request.headers.get("Accept-Language")

    db.save_access_log(created_at, path, x_forwarded, user_agent, languages)

    return empty_js()


@app.route("/admin")
def admin():
    auth = request.authorization

    if auth is None:
        response = Response("Login Required", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})
        return response

    if auth.username == settings.BASIC_USERNAME and auth.password == settings.BASIC_PASSWORD:
        html = render_template_string(template.ADMIN_CONSOLE, access_logs=db.get_access_log())

        response = Response(html)
        response.set_cookie(
            settings.COOKIE_NAME, settings.COOKIE_NAME, max_age=60 * 60 * 24 * 365 * 10, samesite="None", secure=True
        )
        return response

    else:
        response = Response("Login Failed", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})
        return response


def empty_js():
    response = Response('"use strict";', mimetype="application/javascript")

    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True

    return response
