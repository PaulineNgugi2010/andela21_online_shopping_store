import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db= SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class Products(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True)
	description= db.Column(db.String(300))
	price = db.Column(db.Integer)
	
	def __repr__(self):
		return '<products {} {} {}>'.format (self.title, self.description, self.price)



if __name__ == '__main__':
	manager.run()


