from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime    # Import datetime
from data_bol import Item
from data_bol import Bol

def get_client():
    uri = "mongodb+srv://worker01:1407@clusterdb.md2c04v.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client


# add Document to collection at mongoDB
def insert_bol(Bol):
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    docu = {
        "Bol": Bol.getMbl(),
        "Container": Bol.getContainer(),
        "ETA": Bol.getEta(),
        "Note": Bol.getNote(),
        "Truck": Bol.getTruck(),
        "Customer": Bol.getCustomer()
    }

    result = bol_collection.insert_one(docu)  
    print("Inserted document id:", result.inserted_id)

    client.close()


def insert_bol_multiple(bol_number, container_number, eta, note, truck, customer):

    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    docu = {
        "Bol": bol_number,  # Keys in quotes
        "Container": container_number,
        "ETA": eta, #datetime(2023, 11, 1,0,0),  Correct date format
        "Note": note,
        "Truck": truck,
        "Customer": customer
    }

    #Insert Document
    result = bol_collection.insert_one(docu)  # Correct method name
    print("Inserted document id:", result.inserted_id)

    client.close()

# Delete Document 删------------------------------------------------------------
## 搜索BOL号，删除对应的bol

def delete_bol(bol_number):

    client = get_client()
    db = client['wms']
    bol_collection = db['bol']
    
    result = bol_collection.delete_one({"BOL": bol_number})

    # Check if the operation was successful
    if result.deleted_count > 0:
        print("Document with BOL number", bol_number, "was deleted.")
    else:
        print("No document found with BOL number", bol_number)

    client.close()

##搜索container号，删除对应的
def delete_container(container_number):

    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    # Delete the document
    result = bol_collection.delete_one({"Container": container_number})

    # Check if the operation was successful
    if result.deleted_count > 0:
        print("Document with Container number", container_number, "was deleted.")
    else:
        print("No document found with Container number", container_number)

    client.close()

# update document 改------------------------------------------------------------
def update_info(bol_number, key, value):

    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    # 1. 改当前info, 用 $set
    result = bol_collection.update_one(
        {"Bol": bol_number},
        {"$set": {key: value}}
    )

    # Check if the update was successful 
    if result.matched_count > 0:
        if result.modified_count > 0:
            print("Update successful.")
        else:
            print("Document found, but no changes were needed.")
    else:
        print("No documents matched the query. Update not performed.")

    client.close()

def update_add_item(bol_number="", name="", count=0, pallet=0, 
                    cost =0, price=0, status="", vendor="", 
                    vendor_invoice=""):
    
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    # 1. 添加新info进当前bol 用 $push
    # Specify the BOL number you want to search fo
    result = bol_collection.update_one(
        {"Bol": bol_number},
        {"$push": {"Items": {"name": name, 
                             "count": count, 
                             "pallet": pallet, 
                             "cost": cost,
                             "price": price,
                             "status": status,
                             "vendor":vendor,
                             "vendor_invoice":vendor_invoice}}}
    )

    # Check if the update was successful 
    if result.matched_count > 0:
        if result.modified_count > 0:
            print("Update successful.")
        else:
            print("Document found, but no changes were needed.")
    else:
        print("No documents matched the query. Update not performed.")

    client.close()


# 查， 搜索某个bol or container 号，显示整个bol信息-------------------------------
# Specify the BOL number you want to search for
def search_bol(bol_number):

    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    # Count documents
    document_count = bol_collection.count_documents({"BOL": bol_number})

    if document_count > 0:
        documents = bol_collection.find({"BOL": bol_number})
        for doc in documents:
            print(doc)
    else:
        print("No documents found with BOL number", bol_number)

    client.close()

#overload func, 
def search_bol(bol_number):

    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    # Count documents
    try:
        query = {"Bol": bol_number}
        document = bol_collection.find_one(query)

        if document:
            return True
        else:
            return False
    finally:
        client.close()


#search document by container and bol number 在edit window 中使用
def search_bol_container(bol, container):
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    try:
        query = {"Bol": bol, "Container": container}
        document = bol_collection.find_one(query)

        if document:
            return True
        else:
            return False
    finally:
        client.close()

#return document by container and bol number 在edit window 中使用
def get_bol_container(bol, container):
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']
    
    try:
        query = {"Bol": bol, "Container": container}
        document = bol_collection.find_one(query)
        return document
    finally:
        client.close()

# return document by bol number 在pre_view window 中使用
def get_bol(bol):
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    try:
        query = {"Bol": bol}
        document = bol_collection.find_one(query)
        return document
    finally:
        client.close()


# return all bols stored in bol document 在pre_view window 中使用
def get_all_bols():
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    try:
        all_bols = bol_collection.find({})
        return list(all_bols)  # Convert cursor to list
    finally:
        client.close()

# return all bols stored in bol document 以时间为顺序
def get_all_bols_by_eta():
    client = get_client()
    db = client['wms']
    bol_collection = db['bol']

    try:
        all_bols = bol_collection.find({}).sort("ETA", 1)
        return list(all_bols)  # Convert cursor to list
    finally:
        client.close()
        