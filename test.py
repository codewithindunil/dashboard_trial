from flask import Flask,render_template,request

import csv
import joblib
import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import LinearRegression

app=Flask(__name__)

global data_time_set,data_day_set,data_place_set
totOfWeek=np.arange(7)
totOfDay=np.arange(12)
totOfATime=np.arange(15)
predicitCSV=np.arange(3).reshape(1,3)

data_day_set=0
data_time_set=0
data_place_set=0

totOfATime.fill(0)
for loc in range(0, 15):
    data_place_set=loc
    predicitCSV[0][0]=data_day_set
    predicitCSV[0][1]=data_time_set
    predicitCSV[0][2]=loc
    data=predicitCSV[:,0:3]
    clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')
    result_linear=clsfr_linear.predict(data)
    print(result_linear)
    x=np.around(result_linear,decimals=2)
    if(x-(np.around(x,decimals=0))>0.49):
       y=(x-(x-(np.around(x,decimals=0))))+1
    else:
        y=(np.around(x,decimals=0))  
        totOfATime[loc]=totOfATime[loc] + y

print(totOfATime)
