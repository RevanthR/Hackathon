import io,base64
import pandas as pd
from matplotlib import pyplot as plt
#from matplotlib import style

def gatepass():
	img=io.BytesIO()
	dataset=pd.read_csv("dataset.csv")
	print( dataset.head())
	num=int(input("Enter the Roll Number"))
	dataset1=dataset[4*(num-1):4*(num-1)+4]
	plt.figure(figsize=(5,5))
	labels=['sem1','sem2','sem3','sem4']
	colors=['black','yellow','magenta','cyan']
	plt.title('Gatepasses of every semester')
	plt.pie(dataset1['Gatepasses'],labels=labels,colors=colors,startangle=90)
	plt.savefig(img,format='png')
	img.seek(0)
	plot_url=base64.b64encode(img.getvalue()).decode()
	
	return 'data:image/png;base64,{}'.format(plot_url)
