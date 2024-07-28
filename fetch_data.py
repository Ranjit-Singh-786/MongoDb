from pymongo import MongoClient 
from pymongo.errors import PyMongoError 

connection_string = "mongodb+srv://ranjitsingh:<password>@demo.86fki1p.mongodb.net/?retryWrites=true&w=majority&appName=Demo"
client = MongoClient(connection_string)

databases = client.list_database_names()
print("printing databases names : ")
for database in databases:
    print(database)   


db = client['testdb'] # using testdb database
collections = db.list_collection_names()
print("Printing all the collection names")
for collection in collections:
    print(collection)


selected_collection  = db['testcolle']
documents = selected_collection.find()

for document in documents:
    print(document)

print("Thank you")


