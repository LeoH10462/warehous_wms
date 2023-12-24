import mysql.connector
from mysql.connector import Error

#连接数据库，创建连接对象，返回连接对象
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to save the BOL list to the MySQL database
def save_bol_to_database(connection, my_bol_list):
    cursor = connection.cursor()
    for bol in my_bol_list:
        # Assuming 'bol' has attributes like customer_name, container_info, etc.
        query = """INSERT INTO bol_table (customer_name, container_info, other_details)
                   VALUES (%s, %s, %s);"""
        values = (bol.customer_name, bol.container_info, bol.other_details)
        
        cursor.execute(query, values)

    connection.commit()
    cursor.close()
    print("BOL data saved successfully")
