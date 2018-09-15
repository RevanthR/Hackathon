import io,base64
import pandas as pd
from matplotlib import pyplot as plt
#from matplotlib import style

def attendance():
	img=io.BytesIO()
	dataset=pd.read_csv("dataset.csv")
	print( dataset.head())
	#plt.style.use('ggplot')
	num=int(input("Enter the Roll Number"))
	dataset1=dataset[4*(num-1):4*(num-1)+4]
	plt.figure(figsize=(5,5))
	tick_label=['one','two','three','four']
	plt.bar(dataset1['Semester'],dataset1['Attendance'],tick_label=tick_label,width=0.8,color=['red','blue','green','orange'])
	plt.xlabel('semester')
	plt.ylabel('Attandance')
	plt.title('Attendance of every semester')
	plt.savefig(img,format='png')
	img.seek(0)
	plot_url=base64.b64encode(img.getvalue()).decode()
	
	return 'data:image/png;base64,{}'.format(plot_url)
