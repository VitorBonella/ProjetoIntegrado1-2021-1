from app import db
from datetime import datetime
from user import User


class Post(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True)
    post_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_qtd_sacas = db.Column(db.Integer)
    post_active = db.Column(db.Integer)
    post_type = db.Column(db.Integer)

    owner = db.relationship("User", foreign_keys=post_user)

    def __init__(self, user_id, qtd_sacas, post_type):
        self.post_user = user_id
        self.post_qtdSacas = qtd_sacas
        self.post_type = post_type
        self.post_active = 1

    def __repr__(self):
        return "<Post %r>" % self.post_user
