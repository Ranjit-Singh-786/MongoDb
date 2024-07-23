from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
def check_mongo_connection(uri):
    try:
        # Create a MongoClient
        client = MongoClient(uri)
        
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        print("MongoDB connection: Successful")
        
        # Optionally, you can print the databases in the connection
        print("Databases:", client.list_database_names())
    except ConnectionFailure as ce:
        print("MongoDB connection: Failed", ce)
    except Exception as e:
        print("An error occurred", e)

# Replace <username>, <password>, and <cluster-address> with your MongoDB Atlas details
mongo_uri = "mongodb+srv://ranjitsingh:12453696@demo.86fki1p.mongodb.net/?retryWrites=true&w=majority&appName=Demo"
# mongo_uri = "mongodb+srv://ranjitsingh:bEcGAFY3lngxbMY2@demo.86fki1p.mongodb.net/?retryWrites=true&w=majority&appName=Demo"

check_mongo_connection(mongo_uri)
