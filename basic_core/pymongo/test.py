from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.tproj
try:
    empCol = db.products.find()
    for emp in empCol:
        print(emp)
except Exception as e:
    print(e)