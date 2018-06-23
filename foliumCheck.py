
import os
import folium
import pandas as pd
import time
from geopy.geocoders import Nominatim
geolocator = Nominatim()

import pickle
def writePickle(var, filename):
    with open(filename, 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(var, f)
        return
 
def readPickle(filename):
    with open(filename, 'rb') as f:  # Python 3: open(..., 'rb')
        return pickle.load(f)

master = readPickle('../DIAFTE-master/data/master.pkl')
master= master[0]

def mat(st,ma):
    raw = st.split()
    ya=set(raw).intersection(set(ma))
    if(bool(ya)):
        geolocator = Nominatim()
        location = geolocator.geocode(ya)
        tup=(location.latitude,location.longitude)
        print(location)
        print(location.latitude)
        print(location.longitude)
        return tup,ya
    ya='Singapore'
    geolocator = Nominatim()
    location = geolocator.geocode(ya)
    tup=(location.latitude,location.longitude)
    print(location)
    print(location.latitude)
    print(location.longitude)
    return tup,ya

df=pd.read_csv('/Users/samrudhakelkar/Documents/hacks/DIAFTE-master/data/CSSol-2/whole_train.csv')
df=df[['ordering_customer','beneficiary']]
df=df.astype('str')
folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
for index, row in df.iterrows():
    print(row)
    fromTuple, fromCity=mat(str(row['ordering_customer'][0]),master)
    toTuple, toCity=mat(str(row['beneficiary'][0]),master)
    x1, y1 =  fromTuple
    x2, y2 = toTuple 
    folium.CircleMarker(location=[x1, y1],fill=True).add_to(folium_map)
    folium.CircleMarker(location=[x2, y2],fill=True).add_to(folium_map)
#     m = umap(fromCity,fromTuple,toCity,toTuple)
#     display(m)
#     time.sleep(2)
    if index >5:
        break
folium_map