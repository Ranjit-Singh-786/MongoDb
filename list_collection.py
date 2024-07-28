from pymongo import MongoClient
from pymongo.errors import PyMongoError

# MongoDB connection string
connection_string = "mongodb+srv://ranjitsingh:<password>@demo.86fki1p.mongodb.net/?retryWrites=true&w=majority&appName=Demo"

try:
    # Connect to MongoDB
    client = MongoClient(connection_string)
    db = client['testdb']  # Replace 'testdb' with your database name

    # List all collections in the database
    collections = db.list_collection_names()
    print(f"There are {len(collections)} collections in database!")
    print("Collections in the database:")
    for collection in collections:
        print(collection)

except PyMongoError as e:
    print(f"An error occurred with MongoDB: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
