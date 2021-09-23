import flask_login
from sqlalchemy import exc

from app import db
from flask_login import login_required
from app import app
from flask import render_template, flash, redirect
from app.models.annouce_form import AnnouceForm
from app.models.post import Post


@app.route("/announces")
def announces():
    print(Post.query.all())
    return render_template("announces.html", all_lines=Post.query.all())


@app.route("/new_annouce", methods=["GET", "POST"])
@login_required
def new_annouce():
    form = AnnouceForm()
    if form.validate_on_submit():
        annouce_new = Post(user_id=flask_login.current_user.get_id(),
                           qtd_sacas=form.amount.data,
                           post_type=form.annouce_type.data,
                           post_coffe_type=form.coffe_type.data)
        try:
            db.session.add(annouce_new)
            db.session.commit()
            flash("Registrado com sucesso", "success")
            return redirect("/announces")
        except exc.IntegrityError:
            flash("Erro ao criar anuncio", "danger")
            return render_template('create_annouce.html', form=form)
    return render_template("create_annouce.html", form=form)

@app.route("/my_annouce", methods=["GET", "POST"])
@login_required
def my_annouce():
    logged = flask_login.current_user
    for posts in Post.query.filter_by(post_user=logged.get_id()).all():
        print(posts.post_type, posts.post_username, posts.post_coffe_type)
    return render_template("announces.html", all_lines=Post.query.filter_by(post_user=logged.get_id()).all())
