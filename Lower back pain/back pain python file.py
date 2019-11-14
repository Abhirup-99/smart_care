import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score

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

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.30,random_state=2)

from sklearn.linear_model import LogisticRegression
logclf=LogisticRegression(random_state=9, solver='lbfgs', multi_class='ovr',max_iter=200)
logclf.fit(x,y)

#actual computation



pelvic_incidence=50 

pelvic_tilt=50

lumbar_lordosis_angle=40

sacral_slope=67

pelvic_radius=78

degree_spondylolisthesis=79

pelvic_slope=0.4

Direct_tilt=79

thoracic_slope=56

cervical_tilt=68

sacrum_angle=-9

scoliosis_slope=79



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