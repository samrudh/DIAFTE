# imports
import matplotlib.pyplot as plt
import csv
import numpy as np
from mpl_toolkits.basemap import Basemap

import pandas as pd


'''
Function to configure baseplot variable m
'''

def setBaseplot():
    m = Basemap(llcrnrlon=-100.,llcrnrlat=20.,urcrnrlon=20.,urcrnrlat=60.,\
                rsphere=(6378137.00,6356752.3142),\
                resolution='l',projection='merc',\
                lat_0=40.,lon_0=-20.,lat_ts=20.)
    return m

'''
Function to plot image from lat-longs of from city and to city
'''

def plotGeoPlot(m, fromCity, toCity, fromTuple, toTuple):

    fromLat , fromLong = fromTuple
    toLat, toLong = toTuple
    
    # draw great circle route between NY and London
    m.drawgreatcircle(fromLong,fromLat,toLong,toLat,linewidth=2,color='r')
     
    m.drawcoastlines()
    m.fillcontinents(color='lightgreen',lake_color='lightblue')
    
    # draw parallels
    m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
    # draw meridians
    m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
    
    x, y = m(toLong, toLat)  
    plt.text(x, y, toCity,fontsize=12,fontweight='bold', ha='left',va='top',color='blue')
    
    x, y = m(fromLong, fromLat)  

    plt.text(x, y, fromCity, fontsize=12,fontweight='bold',ha='left',va='top',color='k')
    plt.title("Swift Message going from " + fromCity + " to " + toCity);
    plt.show()
    return




fromTuple = (40.78,-73.98)
toTuple = (51.53, 0.08)
fromCity = 'New York'
toCity = 'London'
m =setBaseplot()
plotGeoPlot(m,fromCity, toCity, fromTuple, toTuple)
