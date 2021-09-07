from app import app, db, login_manager
from flask import render_template, flash, redirect, url_for
from app.models.login_form import LoginForm
from app.models.register_form import RegisterForm
from app.models.user import User
from flask_login import login_user, logout_user
from coffe_price_brazil_es import coffee
from sqlalchemy import exc


@login_manager.user_loader
def load_user(id_u):
    return User.query.get(int(id_u))


@app.route("/index")
@app.route("/")
def index():
    return render_template("index_anonymous.html")


@app.route("/register", methods=["GET", "POST"])
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            name=form.name.data,
            phone=form.phone.data
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registrado com sucesso", "success")
            return redirect("/")
        except exc.IntegrityError:
            flash("Já existe uma conta com esses informações", "danger")
            return render_template('register.html', form=form)

        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.user.data).first()
        if u and u.password == form.password.data:
            login_user(u)
            flash("Logou com sucesso", "success")
            return redirect(url_for("index"))
        else:
            flash("Falha ao fazer login", "warning")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logout", "success")
    return redirect(url_for("index"))


@app.route("/announces")
def announces():
    return render_template("announces.html")


@app.route("/infocafe/geral")
def graph_geral():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)


    labels, values0 = coffee.get_prices_by_type("ARABICA RUIM")
    _, values1 = coffee.get_prices_by_type("ARABICA BOM")
    _, values2 = coffee.get_prices_by_type("CONILLON")
    values = [values0, values1, values2]

    return render_template("graph.html", labels=labels, values=values, types=["Arabica ruim", "Arabica bom", "Conillon"], colors=["rgb(0,220,255)", "rgb(0,50,255)", "rgb(63,255,0)"])

@app.route("/infocafe/arabica_ruim")
def graph_arabica_ruim():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)


    labels, values0 = coffee.get_prices_by_type("ARABICA RUIM")
    values = [values0]
    return render_template("graph.html", labels=labels, values=values, types=["Arabica ruim"], colors=["rgb(0,220,255)"])

@app.route("/infocafe/arabica_bom")
def graph_arabica_bom():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)


    labels, values0 = coffee.get_prices_by_type("ARABICA BOM")
    values = [values0]
    return render_template("graph.html", labels=labels, values=values, types=["Arabica bom"], colors=["rgb(0,50,255)"])

@app.route("/infocafe/conillon")
def graph_conillon():

    # labels, values0, values1, values2 = coffee.get_prices_by_range("05/05/2020", "01/01/2022")
    # labels, values0, values1, values2 = coffee.get_prices_by_year(2019)


    labels, values0 = coffee.get_prices_by_type("CONILLON")
    values = [values0]
    return render_template("graph.html", labels=labels, values=values, types=["Conillon"], colors=["rgb(63,255,0)"])