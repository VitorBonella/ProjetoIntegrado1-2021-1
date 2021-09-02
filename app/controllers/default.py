from app import app
from flask import render_template


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/anuncios")
def anuncios():
    return render_template("about.html")