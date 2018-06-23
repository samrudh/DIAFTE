
# from kafka.client import KafkaClient
# from kafka.consumer import SimpleConsumer
from kafka import KafkaConsumer

from datetime import datetime
# import Constants
import json

# import pillow
# img = Image.new('RGBA',(500, 500))

import pandas as pd


import preprocessor
import geoloc


# import time
# from cassandra.policies import DCAwareRoundRobinPolicy



kafkaTopic = 'mt103'




ipaddr = '10.216.7.90'
port = '9092'
connectString = ipaddr + ':' + port
print ("Connecting to Kafka broker at :", connectString)

# cluster = Cluster()
# session = cluster.connect(keysp)
#
# user_insert_stmt = session.prepare("insert into " + tablename+" (timestamp,transactiontime, ask, bid, instrument) values (?,?,?,?,?)");

 
consumer = KafkaConsumer(kafkaTopic, bootstrap_servers=[connectString])
 
# def insert(message):
# #     print ("type is", type(message))
#     msg = json.loads(message.value.decode('ascii'))
#     msg = json.loads(msg)
#
#     format1 = "%Y-%m-%d %H:%M:%S %p %z"
#     transactionT = datetime.strptime(msg["timestamp"], format1)
# #     print ("newType :", type(transactionT))
#
#     return session.execute(user_insert_stmt, [datetime.now()   , transactionT , msg["ask"], msg["bid"], msg["instrument"]])

df = pd.DataFrame()
while True:
    for message in consumer:
            # msg = json.loads(message.value.decode('ascii'))
            # msg = json.loads(msg)
            print("message received :" , eval(message.value))

            ### Parse and get df
            df = preprocessor.get_preprocessed_data(eval(message.value))


            ### Predict



            ## Plot
            geoloc.update_graph_live(df)
            # try:
            #     geoloc.update_graph_live(df)
            # except Exception as e:
            #     print("Exception in visualization module:" + str(e))





