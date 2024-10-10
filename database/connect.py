import pymongo


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
print('connected to mongodb.')
taxi_db = my_client['taxi-drivers']

