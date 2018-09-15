import io,base64
import pandas as pd
from matplotlib import pyplot as plt
#from matplotlib import style

def issues():
	img=io.BytesIO()
	dataset=pd.read_csv("dataset.csv")
	print( dataset.head())
	#plt.style.use('ggplot')
	num=int(input("Enter the Roll Number"))
	dataset1=dataset[4*(num-1):4*(num-1)+4]
	plt.figure(figsize=(5,5))
	plt.hist(dataset1['Issues'],bins=[0,5,10,15,20],edgecolor='black',linewidth=1.2)
	plt.ylabel('issues')
	plt.show()
	plt.savefig(img,format='png')
	img.seek(0)
	plot_url=base64.b64encode(img.getvalue()).decode()
	
	return 'data:image/png;base64,{}'.format(plot_url)
