from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please Enter your First Name")])
	last_name = StringField('Last Name', validators=[DataRequired("Please Enter your Last Name")])
	email = StringField('Email', validators=[DataRequired("Please Enter your E-mail"), Email("Please Enter a valid E-mail")])
	password = PasswordField('Password', validators=[DataRequired("Please Enter a Password"), Length(min=6, message="Password should be atleast 6 characters long")])
	submit = SubmitField('Sign Up')
	
	