import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn import neighbors

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
		data=pd.read_csv('diabetes.csv')
		column=["DiabetesPedigreeFunction"]
		data=data.drop(column,axis=1)
		column=["Outcome"]
		x=data.drop(column,axis=1)
		y=data["Outcome"]
		train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=5)
		knn=neighbors.KNeighborsClassifier(n_neighbors=3,leaf_size=20,p=2)
		knn.fit(x,y)  
		y_pred_KNN = knn.predict(test_x)

		data_preg=num1 #number of pregnancies (0 if male)
		data_glucose=num2 #Plasma glucose concentration  2 hours in an oral glucose tolerance test
		data_bp=num3 #Diastolic blood pressure (mm Hg)
		data_skin=num4 #Triceps skin fold thickness (mm)
		data_insul=num5 #2-Hour serum insulin (mu U/ml)
		data_bmi=num6 #your bmi data
		data_age=num7 #age in years

		pred=knn.predict([[data_preg,data_glucose,data_bp,data_skin,data_insul,data_bmi,data_age]])
		res=pred[0]
		if(res==1):
			self.output_field.insert(0,'')
			self.output_field.insert(0,'Risk')
		else:
			self.output_field.insert(0,'')
			self.output_field.insert(0,'Secure')
	
	def define(self,master):
		self.master=master
		self.label1=Label(master,text="number of pregnancies")
		self.label2=Label(master,text="Plasma glucose concentration")
		self.label3=Label(master,text="Diastolic pressure")
		self.label4=Label(master,text="Triceps skin-fold thickness")
		self.label5=Label(master,text="enter your insulin levels")
		self.label6=Label(master,text="BMI")
		self.label7=Label(master,text="Age")
		self.entry1=Entry(master)
		self.entry2=Entry(master)
		self.entry3=Entry(master)
		self.entry4=Entry(master)
		self.entry5=Entry(master)
		self.entry6=Entry(master)
		self.entry7=Entry(master)
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
		self.button.grid(row=7,column=0)
main(root)
root.title("Diabetes Check")
root.geometry("1600x700")
root.mainloop()
    