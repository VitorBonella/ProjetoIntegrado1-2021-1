from app import app, db, login_manager
from app.models.login_form import LoginForm
from flask import render_template, flash, redirect, url_for
from sqlalchemy import exc
from app.models.register_form import RegisterForm
from app.models.user import User
from flask_login import login_user, logout_user, login_required


@login_manager.user_loader
def load_user(id_u):
    return User.query.get(int(id_u))


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


@app.route('/user/<username>')
@login_required
def user(username):
    print(username)
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
