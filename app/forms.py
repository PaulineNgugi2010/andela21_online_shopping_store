from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length


class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

class ProductsForm(Form):
	title = StringField('Title', validators=[Required(), Length(1, 64)])
	description = StringField('Description', validators=[Required(), Length(1, 300)])
	price = IntegerField('Price', validators=[Required()])
	save = SubmitField('Save')




#class HomeForm(Form):

