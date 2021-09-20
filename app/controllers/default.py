from app import app
from flask import render_template
from coffe_price_brazil_es import coffee


@app.route("/index")
@app.route("/")
def index():
    return render_template("index_anonymous.html")
