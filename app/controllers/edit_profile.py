import flask_login
from sqlalchemy import exc

from app import app
from flask import render_template
from flask_login import login_required
from app.models.edit_form import EditForm

@app.route("/edit_profile")
@login_required
def edit_profile():
    form = EditForm()
    logged = flask_login.current_user
    return render_template("profile.html", form=form, user=logged)
