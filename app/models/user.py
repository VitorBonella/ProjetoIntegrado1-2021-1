from app import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String, unique=True)
    name = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __init__(self, username, password, email, name, phone):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.phone = phone

    def __repr__(self):
        return "<User %r>" % self.username
