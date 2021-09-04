from app import app, db, login_manager
from flask import render_template, flash, redirect, url_for
from app.models.login_form import LoginForm
from app.models.user import User
from flask_login import login_user, logout_user
from coffe_price_brazil_es import coffee


@login_manager.user_loader
def load_user(id_u):
    return User.query.get(int(id_u))


@app.route("/index")
@app.route("/")
def index():
    return render_template("index_anonymous.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.user.data).first()
        if u and u.password == form.password.data:
            login_user(u)
            flash("logou")
            return redirect(url_for("index"))
        else:
            flash("TOMO")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/announces")
def announces():
    return render_template("announces.html")


@app.route("/infocafe/geral")
def graph_test():

    data = coffee.get_table()

    labels = data.index.tolist()
    values = data.iloc[:, 0].tolist()

    return render_template("graph.html", labels=labels, values=values)

