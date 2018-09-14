from flask import Flask,render_template
from graph import h
app=Flask(__name__)

@app.route('/plot')
def chart():
	graph1=h();
	return render_template('graph.html',graph1=graph1)
	
if __name__=="__main__":
	app.run(debug=True,port=8080)