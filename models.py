from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	email = db.Column(db.String(100), unique = True)
	pwhash = db.Column(db.String(100))
	
	def __init__(self, firstname, lastname, email, password):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.email = email.lower()
		self.set_password(password)
	
	def set_password(self, password):
		self.pwhash = generate_password_hash(password)
		
	def check_password_hash(self, password):
		return check_password_hash(self.pwhash, password)