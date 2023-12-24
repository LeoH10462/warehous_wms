import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="DESKTOP-9REDH99",
  user="worker01",
  password="1406",
  database="wms_bol"
)

# Create a cursor object
cursor = mydb.cursor()

# SQL query to insert data
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = ("John", "john@example.com")

# Execute the query
cursor.execute(sql, val)

# Commit the transaction
mydb.commit()

# Close the cursor and connection
cursor.close()
mydb.close()
