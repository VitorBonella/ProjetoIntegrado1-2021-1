from app import app
from flask import render_template


@app.route("/")
def index():
    """ Renderizar a página principal

    :return: Página principal
    :rtype: Template HTML
    """
    return render_template("index_anonymous.html")
