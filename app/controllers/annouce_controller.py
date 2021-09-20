from app import app
from flask import render_template


@app.route("/announces")
def announces():
    return render_template("announces.html")


@app.route("/new_annouce")
def new_annouce():
    return render_template("create_annouce.html")