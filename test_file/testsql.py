import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="JialindeAir.frontiernet.net",
  user="worker01",
  password="14061406",
  database="myDB"
)

# Create a cursor object
cursor = mydb.cursor()

# SQL query to insert data
sql = "INSERT INTO bol (BOL, container, ETA, Date, Note, Truck, customer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ("BOL123", "Container456", "2023-01-01", "2023-01-02", "This is a note", "Truck789", "CustomerXYZ")
cursor.execute(sql, val)
mydb.commit()


# Assume bol_id is the ID of the BOL you just created
bol_id = cursor.lastrowid  # This retrieves the ID of the last inserted row

# Now, insert items related to this BOL
sql = "INSERT INTO item (bol_id, name, count, pallet, item_note, status, cost, sale_price, vendor, vendor_invoice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (bol_id, "ItemName", 10, 5, "Note about the item", "In transit", 100.00, 150.00, "VendorName", "Invoice123")
cursor.execute(sql, val)
mydb.commit()


