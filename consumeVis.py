'''
Created on Oct 12, 2017
@author: Samrudha Kelkar (477255)
'''
from kafka import KafkaConsumer
# from cassandra.cluster import Cluster
from datetime import datetime
import Constants
import json
from random import uniform
## plotting imports
import matplotlib.pyplot as pyplot
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import matplotlib as mpl
from test.test_hash import DatetimeDateTests
plotColor = "green"
red_patch = mpatches.Patch(color=plotColor, label='ask  price')



kafkaTopic = 'mt103'
ipaddr = '10.216.6.51'
port = '9092'

# mpl.style.use('seaborn')
fig = pyplot.figure()
ax1 = fig.add_subplot(111)
# ax1.ylabel('some numbers')
a = 0
b = 10
# kafkaTopic = Constants.kafkaTopic
 
 
ipaddr = Constants.ipaddr
port = Constants.port
connectString = ipaddr + ':' + port
print ("Connecting to Kafka broker at :", connectString)
 
def updatePlot(message):
#     print ("type is", type(message))
    msg = json.loads(message.value.decode('ascii'))
    msg = json.loads(msg)
    
    timestamp = msg["timestamp"]
    ask = msg["ask"]
    format1 = "%Y-%m-%d %H:%M:%S %p %z"
    times = datetime.strptime(timestamp, format1)
    
    return datetime.now()  , float(ask)
 
xval=[]
yval =[]
def drawPlot(k):
    print("updating plot..")
    
    global a
    global b 
    consumer = KafkaConsumer(kafkaTopic, bootstrap_servers=[connectString])
    for message in consumer:
            print("message received :",message)
# #             updatePlot(message)
#             a = uniform(1,10)
#             b = uniform(20,30)
            a , b = updatePlot(message)
            break
    
    tt = 0
    while tt <10:
        tt = tt+1
        xval.append(a)
        yval.append(b)
    ax1.clear()
    ax1.set_xlabel("time")
    ax1.set_ylabel("Ask price (in$)")
#     pyplot.legend("legend")
    pyplot.title("Ask price variations")
    pyplot.legend(handles=[red_patch])
#     fig.xlabel("time")
#     fig.ylabel("ask")
    ax1.plot(xval, yval,  label='axis', color = plotColor)
    
    print("here")
    return
             
ani = animation.FuncAnimation(fig, drawPlot, interval = 1000)
pyplot.show()
    
    
 
 
# while True: 
#     global a 
#     global b
#     