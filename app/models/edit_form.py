from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm


class EditForm(FlaskForm):

    name = StringField("name")
    username = StringField("username")
    email = EmailField('email', [validators.Email()])
    password = PasswordField("password")
    confirm = PasswordField('Repeat Password',
                            [validators.EqualTo("password", message='Senhas não idênticas')])
    phone = StringField('phone')
    submit = SubmitField('Submit')
