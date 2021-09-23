from wtforms import validators
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm
import phonenumbers


class RegisterForm(FlaskForm):

    name = StringField("name", validators=[DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    email = EmailField('email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("password", [validators.DataRequired()])
    confirm = PasswordField('Repeat Password', [validators.DataRequired(), validators.EqualTo("password", message='Senhas não idênticas')])
    phone = StringField('phone', validators=[DataRequired()])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Submit')

