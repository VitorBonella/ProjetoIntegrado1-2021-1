from wtforms import validators
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask import flash
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

    @staticmethod
    def validate_phone(self, phone):
        try:
            if "-" in phone.data:
                phone.data = phone.data.replace("-", "")
            if len(phone.data) == 9:
                if phone.data[0] != '9':
                    flash("Número não começa com 9", "danger")
                    phone.data = ""
                    raise ValidationError('Invalid phone number')
                phone.data = phone.data[0:5] + "-" + phone.data[5:]
            elif len(phone.data) == 8:
                phone.data = phone.data[0:4] + "-" + phone.data[4:]
            phone.data = "+55-27-" + phone.data
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                flash("Número inválido", "danger")
                phone.data = ""
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            flash("Número inválido", "danger")
            phone.data = ""
            raise ValidationError('Invalid phone number')

