from app import app
from flask import render_template


@app.route("/<user>")
@app.route("/", defaults={"user": None})

def index(user):
    return render_template("base.html", data=[1, 2, 3, 4, 5, 6])
