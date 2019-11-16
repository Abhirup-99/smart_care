import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score
from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

root=Tk()
class main:
	def __init__(self,master):
		self.define(master)

	def calculate(self):
		num1 = int(self.entry1.get())
		num2=int(self.entry2.get())
		num3=int(self.entry3.get())
		num4=int(self.entry4.get())
		num5=int(self.entry5.get())
		num6=int(self.entry6.get())
		num7=int(self.entry7.get())
		num8=int(self.entry8.get())
		num9=int(self.entry9.get())
		num10=int(self.entry10.get())
		num11=int(self.entry11.get())
		num12=int(self.entry12.get())
		data=pd.read_csv('Dataset_spine.csv')
		data=data.drop(['Unnamed: 13'], axis=1)
		data=data.rename(columns={"Col1": "pelvic_incidence", "Col2": "pelvic_tilt"})
		data=data.rename(columns={"Col3": "lumbar_lordosis_angle", "Col4": "sacral_slope"})
		data=data.rename(columns={"Col5": "pelvic_radius", "Col6": "degree_spondylolisthesis"})
		data=data.rename(columns={"Col7": "pelvic_slope", "Col8": "Direct_tilt"})
		data=data.rename(columns={"Col9": "thoracic_slope", "Col10": "cervical_tilt"})
		data=data.rename(columns={"Col11": "sacrum_angle", "Col12": "scoliosis_slope"})
		data=data.rename(columns={"Class_att": "result"})
		data=data.replace(["Abnormal", "Normal"], [1,0])
		data['result'] = data['result'].astype('float64')
		column=["result"]
		x=data.drop(column,axis=1)
		y=data["result"]
		train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.30,random_state=2)
		logclf=LogisticRegression(random_state=9, solver='lbfgs', multi_class='ovr',max_iter=200)
		logclf.fit(x,y)

		#actual computation
		pelvic_incidence=num1 
		pelvic_tilt=num2
		lumbar_lordosis_angle=num3
		sacral_slope=num4
		pelvic_radius=num5
		degree_spondylolisthesis=num6
		pelvic_slope=num7
		Direct_tilt=num8
		thoracic_slope=num9
		cervical_tilt=num10
		sacrum_angle=num11
		scoliosis_slope=num12
		result=logclf.predict([[pelvic_incidence,pelvic_tilt,lumbar_lordosis_angle,
		sacral_slope,
		pelvic_radius,
		degree_spondylolisthesis,
		pelvic_slope,
		Direct_tilt,
		thoracic_slope,
		cervical_tilt,
		sacrum_angle,
		scoliosis_slope]])
		final=result[0]
		self.output_field.insert(0,'')
		self.output_field.insert(0,final)
		print('Lower back pain can be caused by a variety of problems with any parts of the complex, interconnected network of spinal muscles, nerves, bones, discs or tendons in the lumbar spine.')
		print('-------------------------------------------------------')
		if (final==1):
		    print('According to the data you provided')
		    print('You have problembs with your back ')
		    print('The condition is not okay and you might have back pain')
		if (final==0):
		    print('According to the data you provided')
		    print('You do not have problems with your back')
		    print('Your condition is okay but still take care')

	def define(self,master):
		self.master=master
		self.label1=Label(master,text="Please enter your value of Pelvic incidence.(In degrees).")
		self.label2=Label(master,text="Please enter your pelvic tilt angle (In degrees).")
		self.label3=Label(master,text="Please enter your value of LLA.(In degrees).")
		self.label4=Label(master,text="Please enter the value in degrees.")
		self.label5=Label(master,text="Please enter your PRA(in degrees).")
		self.label6=Label(master,text="Please mention your degree of spondylolisthesis?")
		self.label7=Label(master,text="Pelvic slope from 0 to 1")
		self.label8a=Label(master,text="Patients with a PT of less than 20 are classified with a PT modifier (0)")
		self.label8b=Label(master,text="Patients with a PT between 20 and 30 are classified with a PT modifier (+)")
		self.label8c=Label(master,text="Patients with a PT of greater than 30 are classified with a PT modifier(++)Please enter your value of tilt?")
		self.label9=Label(master,text="Please enter your value of thoracic slope")
		self.label10=Label(master,text="Please enter your value of cervical tilt")
		self.label11=Label(master,text="Please enter your values")
		self.label12=Label(master,text="Please enter your scoliosis slope.")
		self.entry1=Entry(master)
		self.entry2=Entry(master)
		self.entry3=Entry(master)
		self.entry4=Entry(master)
		self.entry5=Entry(master)
		self.entry6=Entry(master)
		self.entry7=Entry(master)
		self.entry8=Entry(master)
		self.entry9=Entry(master)
		self.entry10=Entry(master)
		self.entry11=Entry(master)
		self.entry12=Entry(master)
		self.button=Button(root,text='Go',fg='Red',command=self.calculate)
		self.output=Label(master,text='Output')
		self.output_field=Entry(master)
		self.output.grid(row=2,column=4)
		self.output_field.grid(row=2,column=5)
		self.label1.grid(row=0,column=0)
		self.entry1.grid(row=0,column=1)
		self.label2.grid(row=1,column=0)
		self.entry2.grid(row=1,column=1)
		self.label3.grid(row=2,column=0)
		self.entry3.grid(row=2,column=1)
		self.label4.grid(row=3,column=0)
		self.entry4.grid(row=3,column=1)
		self.label5.grid(row=4,column=0)
		self.entry5.grid(row=4,column=1)
		self.label6.grid(row=5,column=0)
		self.entry6.grid(row=5,column=1)
		self.label7.grid(row=6,column=0)
		self.entry7.grid(row=6,column=1)
		self.label8a.grid(row=12,column=0)
		self.label8b.grid(row=13,column=0)
		self.label8c.grid(row=14,column=0)
		self.entry8.grid(row=13,column=1)
		self.label9.grid(row=8,column=0)
		self.entry9.grid(row=8,column=1)
		self.label10.grid(row=9,column=0)
		self.entry10.grid(row=9,column=1)
		self.label11.grid(row=10,column=0)
		self.entry11.grid(row=10,column=1)
		self.label12.grid(row=11,column=0)
		self.entry12.grid(row=11,column=1)
		self.button.grid(row=15,column=0)
main(root)
root.title("Lower Back Pain")
root.geometry("1600x700")
root.mainloop()
