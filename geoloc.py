# imports
import matplotlib.pyplot as plt
import csv
import numpy as np
from mpl_toolkits.basemap import Basemap
import pickle
import plotly.plotly as py
import time
import random

import geopy
import pickle
import geoloc
import pandas as pd
import base64
from geopy.geocoders import Nominatim

import matplotlib.image as mpimg


#########################################################
def writePickle(var, filename):
    with open(filename, 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(var, f)
        return

def readPickle(filename):
    with open(filename, 'rb') as f:  # Python 3: open(..., 'rb')
        return pickle.load(f)

# import pandas as pd


def mat(st, ma, geolocator):
    raw = st.split()
    ya = set(raw).intersection(set(ma))
    
    if(bool(ya)):
        ya = list(ya)[0]
        location = geolocator.geocode(ya)
        tup = (location.latitude, location.longitude)
        print(location)
        print(location.latitude)
        print(location.longitude)
        return tup, ya
    ya = 'Singapore'

    location = geolocator.geocode(ya)
    tup = (location.latitude, location.longitude)
    print(location)
    print(location.latitude)
    print(location.longitude)
    return tup, ya


def updateLatLong(row, master, geolocator):
    # df=df[['ordering_customer','beneficiary']]
    # df=df.astype('str')
    # row=df.iloc[0]
    print("df :", row.columns)
    print("row is :", str(row['ordering_customer'][0]))
    fromTuple, fromCity = mat(
        str(row['ordering_customer'][0]), master, geolocator)
    toTuple, toCity = mat(str(row['beneficiary'][0]), master, geolocator)
    return fromCity, toCity, fromTuple, toTuple

# plotGeoPlot(m,fromCity, toCity, fromTuple, toTuple)


def setBaseplot():
    m = Basemap(llcrnrlon=-120., llcrnrlat=-40., urcrnrlon=120., urcrnrlat=70.,
                rsphere=(6378137.00, 6356752.3142),
                resolution='l', projection='merc',
                lat_0=40., lon_0=-20., lat_ts=20.)
    
    return m


'''
Function to plot image from lat-longs of from city and to city
'''


def plotGeoPlot(m, fromCity, toCity, fromTuple, toTuple):

    fromLat, fromLong = fromTuple
    toLat, toLong = toTuple

    # draw great circle route between NY and London
    m.drawgreatcircle(fromLong, fromLat, toLong, toLat, linewidth=2, color='r')

    m.drawcoastlines()
    m.fillcontinents(color='lightgreen', lake_color='lightblue')

    # draw parallels
    m.drawparallels(np.arange(10, 90, 20), labels=[1, 1, 0, 1])
    # draw meridians
    m.drawmeridians(np.arange(-180, 180, 30), labels=[1, 1, 0, 1])

    x, y = m(toLong, toLat)
    plt.text(x, y, toCity, fontsize=12, fontweight='bold',
             ha='left', va='top', color='blue')

    x, y = m(fromLong, fromLat)

    plt.text(x, y, fromCity, fontsize=12, fontweight='bold',
             ha='left', va='top', color='k')
    plt.title("Swift Message going from " +
              str(fromCity) + " to " + str(toCity))
    # plt.show()
    
    # from PIL import Image, ImageDraw
    # img = Image.new('RGBA',(500, 500))
    # if imgplot and imgplot is not None:
    #     imgplot.clf()
    # imgplot = plt.imshow(img)
    # time.sleep(5)
    print("plot graph")
    # plt.show()
    img=mpimg.imread('data/pic.png')
    imgplot = plt.imshow(img)
    plt.show()
    
    return None




def update_graph_live(df):
    

    master = readPickle('data/master.pkl')[0]
    m = geoloc.setBaseplot()



    geolocator = Nominatim()
    
    # df=pd.read_csv('data/CSSol-2/whole_train.csv')
    df=df[['ordering_customer','beneficiary']].reset_index()
    df=df.astype('str')
    row = df.reset_index()
    fromcity, tocity, fromtuple, totuple = updateLatLong(row, master, geolocator)
    fig = plotGeoPlot(m, fromcity, tocity, fromtuple, totuple)
    return fig