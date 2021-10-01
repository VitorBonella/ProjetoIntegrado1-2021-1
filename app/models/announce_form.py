
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired


class AnnouceForm(FlaskForm):

    coffe_type = SelectField("coffe_type", choices=[('1', 'Arabica "Dura"'),
                                                    ('2', 'Arabica "Rio"'),
                                                    ('3', 'Conillon')])
    amount = IntegerField("amount", validators=[DataRequired()])
    annouce_type = RadioField("annouce_type", choices=[('0', 'Venda'), ('1', 'Compra')])

