from flask import Flask,render_template
import os
from graph import h
from gatepass import gatepass
from flask_sqlalchemy import SQLAlchemy
from attendance import attendance
from issues import issues
from backlogs import backlogs

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
@app.route('/cgpa')
def chart():
	graph1=h()
	return render_template('graph.html',graph1=graph1)

@app.route('/gatepass')
def chart2():
	graph2=gatepass()
	return render_template('gatepass.html',graph2=graph2)

@app.route('/attendance')
def chart3():
	graph3=attendance()
	return render_template('attendance.html',graph3=graph3)
@app.route('/issues')	
def chart4():
	graph4=issues()
	return render_template('issues.html',graph4=graph4)	
@app.route('/backlogs')
def chart5():
	graph5=backlogs()
	return render_template('backlogs.html',graph5=graph5)		

if __name__=="__main__":
	app.run(debug=True,port=8080)