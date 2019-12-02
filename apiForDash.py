from flask import Flask,render_template,request
from flask import Flask, jsonify, request
import xmltodict
import csv
import joblib
import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from flask_cors import CORS

app=Flask(__name__)
#core uses for domain errors
CORS(app)

global data_time_set,data_day_set,data_place_set
totOfWeek=np.arange(7)
totOfDay=np.arange(12)
totOfATime=np.arange(15)
predicitCSV=np.arange(3).reshape(1,3)

#total count of week by days
@app.route("/weekTot",methods=['GET','POST'])
def weekTot():
    totOfWeek.fill(0)
    for date in range(0,7):      
        for time in range(0,12):
            for loc in range(0, 15):
                data_place_set=loc
                data_day_set=date
                data_time_set=time
                predicitCSV[0][0]=data_day_set
                predicitCSV[0][1]=data_time_set
                predicitCSV[0][2]=data_place_set
                data=predicitCSV[:,0:3]
                clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')

                result_linear=clsfr_linear.predict(data)
                x=np.around(result_linear,decimals=2)
                if(x-(np.around(x,decimals=0))>0.49):
                    y=(x-(x-(np.around(x,decimals=0))))+1
                else:
                    y=(np.around(x,decimals=0))
                totOfWeek[date]=totOfWeek[date] + y
    return render_template('input.html',answer=totOfWeek)
    x=totOfWeek.tolist()
    return jsonify(x)



#total count of a time range by locations
@app.route("/totOfATime",methods=['GET','POST'])
def totOfATim():
    if request.method=='POST':
        data=request.form
        data_day_set=data['date']
        data_time_set=data['time']
        totOfATime.fill(0)
        for loc in range(0, 15):
            data_place_set=loc
            predicitCSV[0][0]=data_day_set
            predicitCSV[0][1]=data_time_set
            predicitCSV[0][2]=data_place_set
            data=predicitCSV[:,0:3]
            clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')
            result_linear=clsfr_linear.predict(data)
            x=np.around(result_linear,decimals=2)
            if(x-(np.around(x,decimals=0))>0.49):
                y=(x-(x-(np.around(x,decimals=0))))+1
            else:
                y=(np.around(x,decimals=0))  
            totOfATime[loc]=totOfATime[loc] + y
    #return render_template('result.html',answer=totOfATime)
    x=totOfATime.tolist()
    return jsonify(x)



#total count of a day by time ranges
@app.route("/totOfDay",methods=['GET','POST'])
def totOfDa():
    totOfDay.fill(0)
    if request.method=='POST':
        data=request.form
        data_day_set=data['date']
        print(data_day_set)
        totOfDay.fill(0)
        for time in range(0, 12):
            for loc in range(0, 15):
                data_place_set=loc
                #data_day_set=day
                data_time_set=time
                predicitCSV[0][0]=data_day_set
                predicitCSV[0][1]=data_time_set
                predicitCSV[0][2]=data_place_set
                data=predicitCSV[:,0:3]
                clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')

                result_linear=clsfr_linear.predict(data)
                x=np.around(result_linear,decimals=2)
                if(x-(np.around(x,decimals=0))>0.49):
                    y=(x-(x-(np.around(x,decimals=0))))+1
                else:
                    y=(np.around(x,decimals=0))
                totOfDay[time]=totOfDay[time] + y
    #return render_template('result.html',answer=totOfDay)
    x=totOfDay.tolist()
    return jsonify(x)

##@app.route("/predict",methods=['GET','POST'])
##def pred():
##    if request.method=='POST':
##        data=request.form
##        data_place_set=data['loc']
##        data_day_set=data['date']
##        data_time_set=data['time']
##        predicitCSV=[(data_day_set,data_time_set,data_place_set)]
##        csvfile=open('predictCSV.csv','w',newline='')
##        obj=csv.writer(csvfile)
##        for person in predicitCSV:
##            obj.writerow(person)
##            obj.writerow(person)
##        csvfile.close()
##        dataset=pd.read_csv('predictCSV.csv').values
##        data=dataset[:,0:3]
##        clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')
##    result_linear=clsfr_linear.predict(data)
##    return render_template('result.html',answer=result_linear)
####        x=result_linear.tolist()
####        return jsonify(x)










app.run(debug=True)
