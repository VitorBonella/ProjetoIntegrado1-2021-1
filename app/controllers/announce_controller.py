import flask_login
from sqlalchemy import exc

from app import db
from flask_login import login_required
from app import app
from flask import render_template, flash, redirect
from app.models.announce_form import AnnouceForm
from app.models.post import Post


@app.route("/announces")
def announces():
    return render_template("announces.html", all_lines=Post.query.all())


@app.route("/new_announce", methods=["GET", "POST"])
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
            return render_template('create_announce.html', form=form)
    return render_template("create_announce.html", form=form)


@app.route("/my_announces", methods=["GET", "POST"])
@login_required
def my_annouce():
    logged = flask_login.current_user
    return render_template("announces.html", all_lines=Post.query.filter_by(post_user=logged.get_id()).all(), profile=True)


@app.route("/del_announce/<post_id>", methods=["GET", "POST"])
@login_required
def del_annouce(post_id):
    p = Post.query.filter_by(post_id=post_id).first_or_404()
    db.session.delete(p)
    db.session.commit()
    return redirect("/my_announces")


@app.route("/finish_announce/<post_id>", methods=["GET", "POST"])
@login_required
def finish_annouce(post_id):
    p = Post.query.filter_by(post_id=post_id).first_or_404()
    p.post_active = 0
    db.session.commit()
    return redirect("/my_announces")
