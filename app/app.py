from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
#from flask.ext.moment import Moment 
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask.ext.script import Shell
from forms import LoginForm, ProductsForm
import models
from models import db
from models import Products


app= Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
@app.route('/')
def index():
	return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)

@app.route('/displayproducts', methods=['GET', 'POST'])
def view():
		products = Products.query.all()
		return render_template('displayproducts.html', products=products, table=products)

@app.route('/products', methods=['GET', 'POST'])
def products():
	form = ProductsForm(request.form)
	if request.method == 'GET':
		return render_template('products.html', title='Add Products', form=form)
	if request.method == 'POST':	
		title = Products.query.filter_by(title=form.title.data).first()
		products = Products(title= form.title.data,
			description=form.description.data, 
			price=form.price.data)
		db.session.add(products)
		db.session.commit()
		return redirect(url_for('products'))




	# if form.validate_on_submit():
	# 	user = User.query.filter_by(username=form.name.data).first()
	# 	if user is None:
	# 		user = User(username= form.name.data)
	# 		db.session.add(user)
	# 		session['known'] = False
	# 	else:
	# 		session['known'] = True
	# 	session['name'] = form.name.data
	# 	form.name.data = ''
	# 	return redirect(url_for('index'))
	# return render_template('index.html', 
	# 	form = form, name=session.get('name'),
	# 	known = session.get('knoswn', False))

	#return render_template('index.html', form=form, name= session.get('name'))


if __name__ == '__main__':
	app.run(debug=True)