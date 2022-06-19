from flask import render_template, Blueprint, request
import mysql.connector
routes = Blueprint('routes', __name__)

#vars
login_confirm = None
login_confirm == False
sign_up_confirm = False
@routes.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    sign_up_confirm == True
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    password1 = request.form.get('password1')
    if request.method == 'POST':
            db = mysql.connector.connect(
                user='root',
                password='admin',
                host='localhost',
                database='zacks_database')
            cursor = db.cursor()
            insert_stmt = "INSERT INTO cactus_website (email, first_name, password) VALUES (%s, %s, %s)"
            val = (email, first_name, password1)
            cursor.execute(insert_stmt, val)
            db.commit()
            print("data inserted")
            db.close()
            return render_template('home_page.html')
    return render_template('sign_up.html')

    return render_template('base.html')
@routes.route('/website/login', methods=['POST', 'GET'])

def login():
    login2 = True
    login_confirm = True
    email = request.form.get('email')
    password = request.form.get('password1')
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        print(email)
        print(password1)
        db = mysql.connector.connect(
            user='root',
            password='admin',
            host='localhost',
            database='zacks_database')
#        email = 'jim@gmail.com'
        args = [email]
        cursor = db.cursor()
        cursor.callproc('sp_cactus_website', args)

        for result in cursor.stored_results():
            print(result.fetchall())

        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("email = ", row[0]),
            print("password = ", row[1])
            print("name = " , row[2])
        login_confirm = True
        db.commit()
        db.close()
        if cursor.rowcount == 1:
            return render_template("home_page.html")
        else:
            return render_template("login.html")
    return render_template('login.html')
