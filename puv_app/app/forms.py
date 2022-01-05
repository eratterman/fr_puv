from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class PlaceOrderForm(FlaskForm):
    vehicle = SelectField('vehicle', validators=[DataRequired()])
    submit = SubmitField('Order')
