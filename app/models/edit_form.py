from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError
from app.models.user import User
from flask_login import current_user


class EditForm(FlaskForm):

    name = StringField("name")
    username = StringField("username")
    email = EmailField('email', [validators.Email()])
    password = PasswordField("password")
    confirm = PasswordField('Repeat Password')
    phone = StringField('phone', validators=[])
    submit = SubmitField('Submit')

    @staticmethod
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')