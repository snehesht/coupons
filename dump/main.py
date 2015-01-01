from flask import Flask,redirect,render_template,url_for,request,session
from flask.ext.mongoengine import MongoEngine
from mongoengine import *
# Flask app Intilization
app = Flask(__name__)
# MongoDB Settings
app.config['MONGODB_SETTINGS'] = {
	'db' 		: 'coupons',
	'host'		: '127.0.0.1',
	'port'		: 27017
}
# Define MongoDB connection
db = MongoEngine(app)
# Import all other files into a single file
from views import *
from database import *


if __name__=="__main__":
	app.run(debug=True)