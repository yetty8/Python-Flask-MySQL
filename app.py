from flask import Flask, render_template, request, redirect

import logging
from flask_mysqldb import MySQL
import MySQLdb.cursors
import time


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'my_flask_app'

mysql = MySQL(app)

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("App is being executed")

def get_db_connection():
    """Create and return a database connection."""
    return mysql.connection

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            
            name = request.form.get('name')
            city = request.form.get('city')
            email = request.form.get('email')
            age = request.form.get('age')
            gender = request.form.get('gender')
            phone = request.form.get('phone')
            address = request.form.get('address')
            country = request.form.get('country')
            occupation = request.form.get('occupation')

            
            if not all([name, city, email, age, gender, phone, address, country, occupation]):
                return 'Error: All fields are required', 400

            
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('''
                INSERT INTO user_data (name, city, email, age, gender, phone, address, country, occupation)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (name, city, email, age, gender, phone, address, country, occupation))

            mysql.connection.commit()

            
            return redirect('/display')
        except Exception as e:
            print(f"Error: {e}")  
            return f'Error: {e}', 400
    return render_template('form.html')

import time

@app.route('/display')
def display():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_data')  
        data = cursor.fetchall()
        return render_template('display.html', data=data)  
    except Exception as e:        
        print(e) 
        

if __name__ == '__main__':
    app.run(port=5002)