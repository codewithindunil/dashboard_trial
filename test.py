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
##
##data_day_set=0
##data_time_set=0
##data_place_set=0


totOfATime.fill(0)
def totOfDa():
    totOfDay.fill(0)
    for time in range(0, 12):
        for loc in range(0, 15):
                #data_place_set=loc
                #data_day_set=day
                #data_time_set=time
            predicitCSV[0][0]=0
            predicitCSV[0][1]=time
            predicitCSV[0][2]=loc
            data=predicitCSV[:,0:3]
            clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')

            result_linear=clsfr_linear.predict(data)
            x=np.around(result_linear,decimals=2)
            if(x-(np.around(x,decimals=0))>0.49):
                y=(x-(x-(np.around(x,decimals=0))))+1
            else:
                y=(np.around(x,decimals=0))
            totOfDay[time]=totOfDay[time] + y
##          print(totOfDay)
##            print(y)
    print(totOfDay)
totOfATime.fill(0)
def totOfATim():
    for loc in range(0, 15):
        #data_place_set=loc
        predicitCSV[0][0]=5
        predicitCSV[0][1]=10
        predicitCSV[0][2]=loc
        data=predicitCSV[:,0:3]
        clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')
        result_linear=clsfr_linear.predict(data)
        x=np.around(result_linear,decimals=2)
        if(x-(np.around(x,decimals=0))>0.49):
            y=(x-(x-(np.around(x,decimals=0))))+1
        else:
            y=(np.around(x,decimals=0))  
        totOfATime[loc]=totOfATime[loc] + y
        #print(totOfATime)
        #print(y)
    print(totOfATime)


#totOfDa()
totOfATim()

##print(totOfDay)
