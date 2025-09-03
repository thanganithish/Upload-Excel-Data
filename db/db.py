from pymongo import MongoClient

MONGO_URI = "mongodb://192.168.35.50:27017/"
DB_NAME = "code-ez-ide-nitish"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["excel_records"]
