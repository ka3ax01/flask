from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email
class ContactForm(Form):
    name = StringField("Name Of Student")
    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("Address")

    email = StringField("Email")

    Age = IntegerField("age")
    language = SelectField('Languages', choices=[('cpp','c++'),('py','Python')])
    submit = SubmitField("Send")
