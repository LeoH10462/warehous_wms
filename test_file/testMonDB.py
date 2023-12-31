from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime    # Import datetime

# Connect to MongoDB
uri = "mongodb+srv://worker01:1407@clusterdb.md2c04v.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

# Confirm Connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Access Database and Collection
db = client['wms']
bol_collection = db['bol']

# Create Document 增------------------------------------------------------------

def insert_bol(bol_number, container_number, eta, note, truck, customer):
    docu01 = {
        "Bol": bol_number,  # Keys in quotes
        "Container": container_number,
        "ETA": eta, #datetime(2023, 11, 1,0,0),  Correct date format
        "Note": note,
        "Truck": truck,
        "Customer": customer
    }

    #Insert Document
    result01 = bol_collection.insert_one(docu01)  # Correct method name
    print("Inserted document id:", result01.inserted_id)

# Delete Document 删------------------------------------------------------------
## 搜索BOL号，删除对应的bol

def delete_bol(bol_number):
    result01 = bol_collection.delete_one({"BOL": bol_number})

    # Check if the operation was successful
    if result01.deleted_count > 0:
        print("Document with BOL number", bol_number, "was deleted.")
    else:
        print("No document found with BOL number", bol_number)

##搜索container号，删除对应的
def delete_container(container_number):
    # Delete the document
    result = bol_collection.delete_one({"Container": container_number})

    # Check if the operation was successful
    if result.deleted_count > 0:
        print("Document with Container number", container_number, "was deleted.")
    else:
        print("No document found with Container number", container_number)

# update document 改------------------------------------------------------------

def update_bol(bol_number):

    # 1. 改当前info, 用 $set
    result03 = bol_collection.update_one(
        {"BOL": bol_number},
        {"$set": {"Truck": "New Truck"}}
    )

    # Check if the update was successful 
    if result03.matched_count > 0:
        if result03.modified_count > 0:
            print("Update successful.")
        else:
            print("Document found, but no changes were needed.")
    else:
        print("No documents matched the query. Update not performed.")


    # 2. 添加新info进当前bol 用 $push
    result04 = bol_collection.update_one(
        {"BOL": bol_number},
        {"$push": {"Items": {"name": "LUCKY20231231", 
                             "count": 10, 
                             "pallet": 1, 
                             "cost": 12.2,
                             "price": 50,
                             "vendor":"",
                             "vendor_invoice":""}}}
    )

    # Check if the update was successful 
    if result04.matched_count > 0:
        if result04.modified_count > 0:
            print("Update successful.")
        else:
            print("Document found, but no changes were needed.")
    else:
        print("No documents matched the query. Update not performed.")


# 查， 搜索某个bol or container 号，显示整个bol信息-------------------------------
# Specify the BOL number you want to search for
def search_bol(bol_number):

    # Count documents
    document_count = bol_collection.count_documents({"BOL": bol_number})

    if document_count > 0:
        documents = bol_collection.find({"BOL": bol_number})
        for doc in documents:
            print(doc)
    else:
        print("No documents found with BOL number", bol_number)

#search_bol("CMDUNBDN396988")