import mysql.connector
from flask import request
from website.routes import login, sign_up
from website.routes import login_confirm, sign_up_confirm

#connect to database
db = mysql.connector.connect(
user='root',
password='admin',
host='localhost',
database='zacks_database')
email = 'jim@gmail.com'
print(email)
args = ['jim@gmail.com' ]
cursor = db.cursor()
#select_stmt = "SELECT * FROM cactus_website WHERE password = 'camaro';"
#cursor.execute(select_stmt)
cursor.callproc('sp_cactus_website', args)

for result in cursor.stored_results():
    print(result.fetchall())


