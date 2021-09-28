import flask_login
from sqlalchemy import exc
from app import app, db
from flask import render_template, redirect, flash, request
from flask_login import login_required
from app.models.user import User
from app.models.post import Post
from app.models.edit_form import EditForm


@app.route("/edit_profile", methods=["POST", "GET"])
@login_required
def edit_profile():
    form = EditForm()
    logged = flask_login.current_user
    if form.is_submitted():
        if form.confirm.data != form.password.data:
            flash("Senhas diferentes", "danger")
            return render_template('profile.html', form=form, user=logged)
        try:
            user = User.query.filter_by(user_id=logged.get_id()).first_or_404()
            if form.username.data != "":
                if not User.query.filter_by(username=form.username.data).first():
                    user.username = form.username.data
                    posts_usuario = Post.query.filter_by(post_user=logged.get_id()).all()
                    for post in posts_usuario:
                        post.post_username = user.username
                else:
                    flash("Usuário já existe", "danger")
                    return render_template('profile.html', form=form, user=logged)
            if form.name.data != "":
                user.name = form.name.data
            if form.email.data != "":
                user.email = form.email.data
                if not User.query.filter_by(email=form.email.data).first():
                    user.email = form.email.data
                else:
                    flash("Email já cadastrado", "danger")
                    return render_template('profile.html', form=form, user=logged)
            if form.phone.data != "":
                user.phone = form.phone.data
                if not User.query.filter_by(phone=form.phone.data).first():
                    user.phone = form.phone.data
                else:
                    flash("Telefone já cadastrado", "danger")
                    return render_template('profile.html', form=form, user=logged)
            if form.password.data != "":
                user.password = form.password.data
            db.session.commit()
            flash("Dados alterados com sucesso", "success")
            return redirect("/")
        except exc.IntegrityError:
            flash("Já existe uma conta com esses informações", "danger")
            return render_template('profile.html', form=form, user=logged)

    return render_template("profile.html", form=form, user=logged)
