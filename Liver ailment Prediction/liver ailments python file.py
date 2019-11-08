import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score


from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#the necessary libraries are imported

data=pd.read_csv('liver_patient.csv')
data=data.dropna()
data = data.rename(columns = {"Dataset": "With Liver Ailment"}) 
data.Gender = data.Gender.replace({"Female": "1", "Male": "2"})
column=["With Liver Ailment"]
x=data.drop(column,axis=1)
y=data["With Liver Ailment"]

train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=7)
from sklearn import tree
dtree = tree.DecisionTreeClassifier(criterion='gini',max_depth=20,min_samples_leaf=7,min_samples_split=7)
dtree=dtree.fit(x,y)
res=dtree.predict([[67,1,6,8,600,69,89,7,9,0.9]])
val=res[0]


#actual computation
age=23 #the persons age
gen=2 #female =1, male=2
tb=11 #Total_Bilirubin
db=2 #Direct_Bilirubin
ap=100 #Alkaline_Phosphotase
aa=10 #Alamine_Aminotransferase
aat=50 #Aspartate_Aminotransferase
tp=4 #Total_Protiens
ab=2 #Albumin
agr=0.7 #Albumin_and_Globulin_Ratio

#actual computation
res=dtree.predict([[age,gen,tb,db,ap,aa,aat,tp,ab,agr]])
val=res[0]

if (val==1):
    print('Based on chemical compounds(bilrubin,albumin,protiens,alkaline phosphatase etc )')
    print('You have high risk of liver ailments')
    print('You must get proper treatment')
    print('--------------------------------------------')
    print('Excessive consumption of alcohol, inhale of harmful gases, intake of contaminated food, pickles and drugs')
    print('Highly contribute to liver ailments, if you have been taking any of them, please stop')
    print('--------------------------------------------')
    
    print('===BILIRUBIN===')
    if (tb<=1.4 and db<=0.4):
        print('Normal Bilirubin Levels')
        print('It is normal to have some bilirubin in the blood.')
    else:
        print('Your Bilirubin Levels are higher than above')
        print('High levels of bilirubin can cause many many liver related problembs')
        print('These may be the problembs')
        print('Jaundice, Scarring of the liver (cirrhosis)')
        print('Swollen and inflamed liver (hepatitis)')
        print('Other liver disease')
    
    print('                            ')
    print('===Alkaline_Phosphotase===')
    if (ap<=200):
        print('Alkaline phosphatase (ALP) is an enzyme in a persons blood that helps break down proteins. ')
        print('Your levels are normal')
    else:
        print("Your levels are high")
        print('Slightly irregular ALP levels are usually no cause for concern.')
        print('However, severely abnormal levels can signify a severe underlying medical condition')
        print('Typically one relating to the liver, bones, or gallbladder.')
    
    print('  ')
    print("Total Proteins*************")
    if(tp>=6 and tp<=9):
        print('Your total protein levels are normal')
    else:
        print('Your total protein levels are not okay')
    
 
if (val==0):
    print('Based on chemical compounds(bilrubin,albumin,protiens,alkaline phosphatase etc ')
    print('You have low risk of liver ailments')
    print('===BILIRUBIN===')
    if (tb<=1.4 and db<=0.4):
        print('Normal Bilirubin Levels')
        print('It is normal to have some bilirubin in the blood.')
    else:
        print('Your Bilirubin Levels are higher than above')
        print('High levels of bilirubin can cause many many liver related problembs')
        print('These may be the problembs')
        print('Jaundice, Scarring of the liver (cirrhosis)')
        print('Swollen and inflamed liver (hepatitis)')
        print('Other liver disease')
    
    print('                            ')
    print('===Alkaline_Phosphotase===')
    if (ap<=200):
        print('Alkaline phosphatase (ALP) is an enzyme in a persons blood that helps break down proteins. ')
        print('Your levels are normal')
    else:
        print("Your levels are high")
        print('Slightly irregular ALP levels are usually no cause for concern.')
        print('However, severely abnormal levels can signify a severe underlying medical condition')
        print('Typically one relating to the liver, bones, or gallbladder.')
    
    print('  ')
    print("Total Proteins*************")
    if(tp>=6 and tp<=9):
        print('Your total protein levels are normal')
    else:
        print('Your total protein levels are not okay')
    