from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__) 

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwerty123'
app.config['MYSQL_DB'] = 'batch_5'

mysql = MySQL(app)

@app.route('/') 
def hello_world(): 
    return render_template("my_form.html", my_page_heading = "My form heading", the_num = 20)

@app.route('/contact/', methods = ["POST", "GET"]) 
def hello_contact(): 
    if request.method == "POST":
        u_name = request.form['user_name']
        u_city = request.form['user_city']
        u_age = request.form['user_age']
        u_hobby = request.form['user_hobby']
        my_statement = "Your name is - " + u_name + " and your city is - " + u_city
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        my_insert_query = "INSERT INTO user_data VALUES ('{0}', {1}, '{2}', '{3}')".format(u_name, u_age, u_city, u_hobby)

        cursor.execute(my_insert_query)
        mysql.connection.commit()

        return my_statement
    else:
        return 'Hello contact Get'
    

@app.route('/home/') 
def hello_home(): 
    my_dictionary = {"name": "John Doe", "City": "Toronto"}
    my_list = ["Apple", "mango", "Orange", "Banana", "Pear"]
    return render_template("hello_home.html", the_dictionary = my_dictionary, the_list = my_list)

@app.route('/users/') 
def list_users(): 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    my_select_query = "SELECT * FROM  user_data;"
    cursor.execute(my_select_query)
    data = cursor.fetchall()
    return render_template("users.html",users_data = data)


if __name__ == '__main__': 
	app.run(port=8012, debug=True)