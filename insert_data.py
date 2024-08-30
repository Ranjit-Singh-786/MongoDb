print("heyy i did something here ANSHIKA")
from pymongo import MongoClient
# MongoDB connection string
connection_string = "mongodb+srv://ranjitsingh:<password>@demo.86fki1p.mongodb.net/?retryWrites=true&w=majority&appName=Demo"


    # Connect to MongoDB
client = MongoClient(connection_string)
db = client['testdb']
collection = db['testcolle']

    # Data to be inserted
data = {
    'name': 'Ranjit Singh',
    'city': 'Mathura',
    'profession': 'Data Scientist'
}

    # Insert data into the collection
inserted_id = collection.insert_one(data).inserted_id
print(f"Data inserted with ID: {inserted_id}")



