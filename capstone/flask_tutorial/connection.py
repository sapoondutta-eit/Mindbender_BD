import MySQLdb 
from flask import Flask, render_template 
from flask import Flask, jsonify, Response
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask import Flask, redirect, url_for,request, render_template
import pandas as pd
import matplotlib.pyplot  as plt



app = Flask(__name__)
api = Api(app)


conn = MySQLdb.connect("localhost","root","password","tweets" ) 
cursor = conn.cursor() 

@app.route('/dashboard/')
def example(): 
    cursor.execute("select * from senti_tweets") 
    data = cursor.fetchall() #data from database 
    return render_template("dashboard.html", value=data)

@app.route('/plot/')
def plot():

	cursor.execute("select polarity,subjectivity from senti_tweets")
	result = cursor.fetchall()
	df = pd.DataFrame(list(result),columns=["polarity","subjectivity"])
	x = df.polarity
	y = df.subjectivity
	# Set x-axis range
	plt.xlim((-10,10))
	# Set y-axis range
	plt.ylim((-10,10))
	plt.title("polarity-subjectivity scatter plot", fontsize="24")
	plt.scatter(x, y, s=100)
	plt.xlabel("polarity")
	plt.ylabel("subjectivity")
	plt.axhline(0, color='red')
	plt.axvline(0, color='red')
	plt.tick_params(axis='both',which='major',labelsize=14)
	plt.savefig('static/images/plot.png')
	return render_template('plot.html', url='/static/images/plot.png')



@app.route('/polarity/')
def polarity():
	cursor.execute("select AVG(polarity) from senti_tweets")
	polar = cursor.fetchall()
	df = pd.DataFrame(polar,columns=["polarity"])
	plt.bar(df.polarity,3)
	plt.xlabel("polarity")
	plt.savefig("static/images/polarity.png")
	return render_template("polarity.html",url="static/images/polarity.png")
	




if __name__ == '__main__':
   app.run(debug = True)