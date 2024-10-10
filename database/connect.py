import pymongo


my_client = pymongo.MongoClient("mongodb://localhost:27017/")

print('connected to mongodb.')

crashes_db = my_client['crashes_db']

crashes = crashes_db['crashes']

beats = crashes_db['beats']

