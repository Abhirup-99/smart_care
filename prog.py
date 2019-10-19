import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from tkinter import *

import matplotlib.pyplot as plt

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
		data=pd.read_csv('cardio_train.csv',sep=";")
		data.head(5)
		data['age']=data['age']/365
		column=["id","cardio"]
		x=data.drop(column,axis=1)
		y=data["cardio"]
		y=y.astype(int)
		train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=7)
		classifier = RandomForestClassifier(n_estimators=100,random_state=7,max_depth=10)
		classifier.fit(train_x,train_y)
		y_pred_RF = classifier.predict(test_x)
		data_age=num1   #age of person in years
		data_gender=num2#gender of person 1 - women, 2 - men
		data_height=num3 #height of person in cm
		data_weight=num4 #weight of a person in kg
		data_sys=num5 #systolic blood pressure of person
		data_dia=num6 #diastolic blood pressure of person
		data_cho=num7 # cholestrol levels  1: normal, 2: above normal, 3: well above normal
		data_glu=num8 #blood glucose levels 1: normal, 2: above normal, 3: well above 
		data_smoke=num9 #whether patient smokes or not 1= smoke , 0=non smoker
		data_alco=num10 #whether person is alcoholic or not 1= YES , 0=NO
		data_active=num11 # whether person is engaged in regular sports or exercise
		res=classifier.predict([[data_age,data_gender,data_height,data_weight,data_sys,data_dia,data_cho,data_glu,data_smoke,data_alco,data_active]])
		value=res[0]
		self.output_field.insert(0,'')
		self.output_field.insert(0,value)
	def define(self,master):
		self.master=master
		self.label1=Label(master,text="age")
		self.label2=Label(master,text="gender")
		self.label3=Label(master,text="height")
		self.label4=Label(master,text="weight")
		self.label5=Label(master,text="systolic pressure")
		self.label6=Label(master,text="diastolic pressure")
		self.label7=Label(master,text="cholestrol levels")
		self.label8=Label(master,text="glucose levels")
		self.label9=Label(master,text="smoke")
		self.label10=Label(master,text="alcoholic")
		self.label11=Label(master,text="active")
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
		self.button=Button(root,text='Go',fg='Red',command=self.calculate)
		self.output=Label(master,text='Output')
		self.output_field=Entry(master)
		self.output.grid(row=2,column=4)
		self.output_field.grid(row=2,column=5)
		self.label1.grid(row=0,column=0)
		self.entry1.grid(row=0,column=1)
		self.label2.grid(row=0,column=2)
		self.entry2.grid(row=0,column=3)
		self.label3.grid(row=0,column=4)
		self.entry3.grid(row=0,column=5)
		self.label4.grid(row=0,column=6)
		self.entry4.grid(row=0,column=7)
		self.label5.grid(row=0,column=8)
		self.entry5.grid(row=0,column=9)
		self.label6.grid(row=0,column=10)
		self.entry6.grid(row=0,column=11)
		self.label7.grid(row=1,column=1)
		self.entry7.grid(row=1,column=2)
		self.label8.grid(row=1,column=3)
		self.entry8.grid(row=1,column=4)
		self.label9.grid(row=1,column=5)
		self.entry9.grid(row=1,column=6)
		self.label10.grid(row=1,column=7)
		self.entry10.grid(row=1,column=8)
		self.label11.grid(row=1,column=9)
		self.entry11.grid(row=1,column=10)
		self.button.grid(row=2,column=1)
main(root)
root.title("Cardio Vascular Check")
root.geometry("1600x700")
root.mainloop()
