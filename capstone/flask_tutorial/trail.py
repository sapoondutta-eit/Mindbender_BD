import MySQLdb 
from flask import Flask, render_template 
from flask import Flask, jsonify, Response
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask import Flask, redirect, url_for,request, render_template



app = Flask(__name__)
api = Api(app)


conn = MySQLdb.connect("localhost","root","password","tweets" ) 
cursor = conn.cursor() 

@app.route('/dashboard/')
def example(): 
    cursor.execute("select * from senti_tweets") 
    data = cursor.fetchall() #data from database 
    return render_template("dashboard.html", value=data)




if __name__ == '__main__':
   app.run(debug = True)