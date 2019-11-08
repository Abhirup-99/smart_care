import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score


from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data=pd.read_csv('diabetes.csv')
column=["DiabetesPedigreeFunction"]
data=data.drop(column,axis=1)
column=["Outcome"]
x=data.drop(column,axis=1)
y=data["Outcome"]
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=5)
from sklearn import neighbors
knn=neighbors.KNeighborsClassifier(n_neighbors=3,leaf_size=20,p=2)
knn.fit(x,y)  
y_pred_KNN = knn.predict(test_x)

data_preg=0 #number of pregnancies (0 if male)
data_glucose=130 #Plasma glucose concentration  2 hours in an oral glucose tolerance test
data_bp=95 #Diastolic blood pressure (mm Hg)
data_skin=10 #Triceps skin fold thickness (mm)
data_insul=100 #2-Hour serum insulin (mu U/ml)
data_bmi=24 #your bmi data
data_age=27 #age in years

pred=knn.predict([[data_preg,data_glucose,data_bp,data_skin,data_insul,data_bmi,data_age]])
res=pred[0]
if(res==1):
    print('According to the data you provided and the data we have- ')
    print('You have high risk of Diabetes')
    print('Please mend your ways.')
    print('High level of sugar is highly related to diabetes')
    print('High BMI also has corelation to Diabetes')
else:
    print('According to the data you provided and the data we have- ')
    print('You have low risk of diabetes. ')
    print('Please maintain your healthy life style')