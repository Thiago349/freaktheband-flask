import flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import os
import smtplib
import email.message


app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DATABASE')

mysql = MySQL(app)

@app.route('/news')
def news_db():
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM news ORDER BY id DESC LIMIT 3")
    fetchdata = cur.fetchall()
    fetchdata = jsonify(fetchdata)
    return fetchdata

@app.route('/events')
def events_db():
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM events")
    fetchdata = cur.fetchall()
    fetchdata = jsonify(fetchdata)
    return fetchdata

@app.route('/rocksession')
def rocksession_db():
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM rocksession")
    fetchdata = cur.fetchall()
    fetchdata = jsonify(fetchdata)
    return fetchdata

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.run(debug=False)
