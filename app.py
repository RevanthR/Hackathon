from flask import Flask,render_template
import os
from graph import h
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Puppy(db.Model):
	__tablename__='puppies'

	id = db.Column(db.Integer,primary_key=True)
	name=db.Column(db.Text)
	age=db.Column(db.Integer)

	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __repr__(self):
		return f"Puppy {self.name} is {self.age} yearsr old"	
@app.route('/plot')
def chart():
	graph1=h();
	return render_template('graph.html',graph1=graph1)
	
if __name__=="__main__":
	app.run(debug=True,port=8080)