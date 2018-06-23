"Configration parameters"


kafkaTopic = 'mt103'
ipaddr = '10.216.7.90'
port = '9092'
confParameters = {"keyspace": "demo", "table": "project1"}
keyspacename = confParameters["keyspace"]
tablename = confParameters["table"]
queryConf = {"Highest": True, "Lowest": True, "HighestDelta": True, "LowestDelta": True,\
             "Avg":True, "StdDev": True}

