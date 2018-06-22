# imports
import matplotlib.pyplot as plt
import csv
import numpy as np
from mpl_toolkits.basemap import Basemap

import pandas as pd

# filename=  'latlongdata.csv'
# 
# d = {'TouchDownLat': [31.53, 46.45, 43.1 ], 'TouchDownLong': [-97.15, -100.67 , -83.85] , 'LiftoffLat': [31.74,46.67,43.17], 'LiftoffLong':[-96.88,-100.47,-83.42]}
# df = pd.DataFrame(data=d)
# # 
# # df.to_csv('latlongdata.csv', header=True)
#     
# lat_td =df['TouchDownLat'].tolist()
# long_td = df['TouchDownLong'].tolist()
# lat_lift = df['LiftoffLat'].tolist()
# long_lift = df['LiftoffLong'].tolist()
# 
# touchdown = np.array([[lat_td], [long_td]])
# lift = np.array([[lat_lift], [long_lift]])
# 
# ### Geoplots
# m = Basemap(projection = 'merc', llcrnrlat=float(min(lat_td)) - 2,\
#     urcrnrlat=float(max(lat_lift)) + 2, llcrnrlon=float(max(long_td)) - 2,\
#     urcrnrlon=float(min(long_lift)) + 2,lat_ts=40,resolution='l')
#  
# lat = df['TouchDownLat'].tolist() 
# lon = df['TouchDownLong'].tolist() 
# #  
# # x, y = m(lon, lat)
# # m.plot(x, y, 'o-', markersize=5, linewidth=1) 
# #  
# # m.drawcoastlines()
# # m.fillcontinents(color='white')
# # m.drawmapboundary(fill_color='white')
# # m.drawstates(color='black')
# # m.drawcountries(color='black')
# # plt.title("#wedgez")
# # plt.show() 
# 
# # set up orthographic map projection with
# # perspective of satellite looking down at 50N, 100W.
# # use low resolution coastlines.
# map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# # draw coastlines, country boundaries, fill continents.
# map.drawcoastlines(linewidth=0.25)
# map.drawcountries(linewidth=0.25)
# # map.fillcontinents(color='coral',lake_color='aqua')
# # draw the edge of the map projection region (the projection limb)
# map.drawmapboundary(fill_color='aqua')
# # draw lat/lon grid lines every 30 degrees.
# # map.drawmeridians(np.arange(0,360,30))
# # map.drawparallels(np.arange(-90,90,30))
# # make up some data on a regular lat/lon grid.
# nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
# lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
# lons = (delta*np.indices((nlats,nlons))[1,:,:])
# wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
# mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# # compute native map projection coordinates of lat/lon grid.
# x, y = map(lons*180./np.pi, lats*180./np.pi)
# # contour data over the map.
# hyd = [17.3850, 78.486]
# singapore = [1.3521, 103.8198]
# cs = map.plot(x,y)
# # plt.title('contour lines over filled continent background')
# plt.show()


# create new figure, axes instances.
# fig=plt.figure(figsize=(12, 8) )
# ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.



m = Basemap(llcrnrlon=-100.,llcrnrlat=20.,urcrnrlon=20.,urcrnrlat=60.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)


# nylat, nylon are lat/lon of New York
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53; lonlon = 0.08
# draw great circle route between NY and London
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='r')
 
m.drawcoastlines()
m.fillcontinents(color='lightgreen',lake_color='lightblue')

# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])

x, y = m(lonlon, lonlat)  
plt.text(x, y, 'London',fontsize=12,fontweight='bold', ha='left',va='top',color='blue')

x, y = m(nylon, nylat)  

plt.text(x, y, 'New York',fontsize=12,fontweight='bold',ha='left',va='top',color='k')
plt.title('Great Circle from New York to London');
plt.show()


