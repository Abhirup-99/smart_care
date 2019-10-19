import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score


from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data=pd.read_csv('cardio_train.csv',sep=";")
data.head(5)

data['age']=data['age']/365

column=["id","cardio"]
x=data.drop(column,axis=1)
y=data["cardio"]
y=y.astype(int)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=7)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100,random_state=7,max_depth=10)
classifier.fit(train_x,train_y)
y_pred_RF = classifier.predict(test_x)

data_age=19   #age of person in years
data_gender=2#gender of person 1 - women, 2 - men
data_height=178 #height of person in cm
data_weight=70 #weight of a person in kg
data_sys=150 #systolic blood pressure of person
data_dia=70 #diastolic blood pressure of person
data_cho= 1 # cholestrol levels  1: normal, 2: above normal, 3: well above normal
data_glu=1 #blood glucose levels 1: normal, 2: above normal, 3: well above 
data_smoke=1 #whether patient smokes or not 1= smoke , 0=non smoker
data_alco=1 #whether person is alcoholic or not 1= YES , 0=NO
data_active=1 # whether person is engaged in regular sports or exercise

res=classifier.predict([[data_age,data_gender,data_height,data_weight,data_sys,data_dia,data_cho,data_glu,data_smoke,data_alco,data_active]])


value=res[0]
print(value)