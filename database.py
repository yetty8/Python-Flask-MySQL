import mysql.connector
import os

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'localhost'),
        user=os.environ.get('MYSQL_USER', 'Yetty'),  
        password=os.environ.get('MYSQL_PASSWORD', 'Yetty123'),  
        database=os.environ.get('MYSQL_DB', 'my_flask_app')
    )
    return connection

def insert_data(name, city, age, email, phone, address, country, state, zip_code, occupation):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO your_table (name, city, age, email, phone, address, country, state, zip_code, occupation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                   (name, city, age, email, phone, address, country, state, zip_code, occupation))
    connection.commit()
    cursor.close()
    connection.close()

def fetch_data():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT my_flask_app')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
