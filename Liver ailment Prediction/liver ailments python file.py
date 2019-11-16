import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tkinter import *
from sklearn import tree
#the necessary libraries are imported

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
        data=pd.read_csv('liver_patient.csv')
        data=data.dropna()
        data = data.rename(columns = {"Dataset": "With Liver Ailment"}) 
        data.Gender = data.Gender.replace({"Female": "1", "Male": "2"})
        column=["With Liver Ailment"]
        x=data.drop(column,axis=1)
        y=data["With Liver Ailment"]

        train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=7)
        dtree = tree.DecisionTreeClassifier(criterion='gini',max_depth=20,min_samples_leaf=7,min_samples_split=7)
        dtree=dtree.fit(x,y)
        res=dtree.predict([[67,1,6,8,600,69,89,7,9,0.9]])
        val=res[0]


        #actual computation
        age=num1 #the persons age
        gen=num2 #female =1, male=2
        tb=num3 #Total_Bilirubin
        db=num4 #Direct_Bilirubin
        ap=num5 #Alkaline_Phosphotase
        aa=num6 #Alamine_Aminotransferase
        aat=num7 #Aspartate_Aminotransferase
        tp=num8 #Total_Protiens
        ab=num9 #Albumin
        agr=num10 #Albumin_and_Globulin_Ratio

        #actual computation
        res=dtree.predict([[age,gen,tb,db,ap,aa,aat,tp,ab,agr]])
        val=res[0]

        if (val==1):
            self.output_field1.insert(0,'')
            self.output_field1.insert(0,'Risk')
            if (tb<=1.4 and db<=0.4):
                self.output_field2.insert(0,'')
                self.output_field2.insert(0,'Normal Bilirubin levels')
            else:
                self.output_field2.insert(0,'')
                self.output_field2.insert(0,'Bilirubin levels higher')
            
         
        if (val==0):
            self.output_field1.insert(0,'')
            self.output_field1.insert(0,'Safe')
            if (tb<=1.4 and db<=0.4):
                self.output_field2.insert(0,'')
                self.output_field2.insert(0,'Normal Bilirubin levels')
            else:
                self.output_field2.insert(0,'')
                self.output_field2.insert(0,'Bilirubin levels higher')

    def define(self,master):
        self.master=master
        self.label1=Label(master,text="age")
        self.label2=Label(master,text="gender(1 - women, 2 - men)")
        self.label3=Label(master,text="height(in cms)")
        self.label4=Label(master,text="Total Bilirubin")
        self.label5=Label(master,text="Direct Bilirubin")
        self.label6=Label(master,text="Alkaline Phosphotase")
        self.label7=Label(master,text="Alamine Aminotransferase")
        self.label8=Label(master,text="Total Protiens")
        self.label9=Label(master,text="Albumin")
        self.label10=Label(master,text="Albumin and Globulin Ratio")
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
        self.button=Button(root,text='Go',fg='Red',command=self.calculate)
        self.output=Label(master,text='Output')
        self.output_field1=Entry(master)
        self.output_field2=Entry(master)
        self.output.grid(row=2,column=4)
        self.output_field1.grid(row=2,column=5)
        self.output_field2.grid(row=2,column=6)
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
        self.label8.grid(row=7,column=0)
        self.entry8.grid(row=7,column=1)
        self.label9.grid(row=8,column=0)
        self.entry9.grid(row=8,column=1)
        self.label10.grid(row=9,column=0)
        self.entry10.grid(row=9,column=1)
        self.button.grid(row=10,column=0)
main(root)
root.title("Liver Ailments Check")
root.geometry("1600x700")
root.mainloop()
    