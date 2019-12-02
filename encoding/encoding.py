from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# define example
dat = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
tim = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12', '12-14', '14-16', '16-18', '18-20', '20-22','22-24']
loct = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12', 'col13', 'col14', 'col15']
dates = array(dat)
times = array(tim)
locations = array(loct)
#print(values)
# integer encode
label_encoder = LabelEncoder()
day_encoded = label_encoder.fit_transform(dates)
time_encoded = label_encoder.fit_transform(times)
loc_encoded = label_encoder.fit_transform(locations)
#print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
day_encoded = day_encoded.reshape(len(day_encoded), 1)
time_encoded = time_encoded.reshape(len(time_encoded), 1)
loc_encoded = day_encoded.reshape(len(day_encoded), 1)
day_e = onehot_encoder.fit_transform(day_encoded)
time_e = onehot_encoder.fit_transform(time_encoded)
loc_e = onehot_encoder.fit_transform(loc_encoded)
#print(onehot_encoded)
# invert first example
day = label_encoder.inverse_transform([argmax(day_e[:, :])])
time = label_encoder.inverse_transform([argmax(time_e[:, :])])
loc = label_encoder.inverse_transform([argmax(loc_e[:, :])])
print(day)
print(time)
print(loc)
