from flask import Flask,redirect,render_template,url_for,request,session
from flask.ext.mongoengine import MongoEngine
import datetime
# Flask app Intilization
app = Flask(__name__)
# MongoDB Settings
app.config['MONGODB_SETTINGS'] = {
	'db' 		: 'freecharge',
	'host'		: '127.0.0.1',
	'port'		: 27017
}
# Define MongoDB connection
db = MongoEngine(app)

##### Datebase Schema ##############################
# Import all other files into a single file

# Notes
# ExpiryDate datetime.date(2014,12,20).strftime('%d%m%Y')  == 30122014
#
class CouponCode(db.Document):
	uid = db.StringField(required=True)
	date = db.DateTimeField(default=datetime.datetime.now)
	expirydate = db.DateTimeField(required=True)
	status = db.StringField(default="# Active")
	title = db.StringField(required=True)
	category = db.StringField(required=True)
	categoryid = db.IntField(required=False)
	subcategory = db.StringField(required=True)  # Prepaid | PostPaid | DTH 
	description = db.StringField(required=True)
	coupon = db.StringField(required=True)
	like = db.IntField()
	dislike = db.IntField()
	
#	def IsCouponExpired(date,expirydate):
#		if date.strftime('%d%m%Y') == expirydate.strftime('%d%m%Y'):
#			return True
#		else : 
#			return False

#	def buildURL(self.date,self.title):
#		return url_for('couponView', kwargs={"uid":self.uid,"title":self.title})

class Users(db.Document):
	uid = db.IntField(required=True)
	name = db.StringField(required=True)
	email = db.StringField(required=True)
	password = db.StringField(required=True)




#####*********** Views & Routing **********#####
## 1. Default View
##
@app.route('/')
@app.route('/index')
def index():
#	new = CouponCode(uid='05c2aacxH',expirydate=datetime.date(2014,12,31),
#		title="Rs.100 Off on recharge of Rs.500 or above",category="FreeCharge",
#		categoryid=2,subcategory="Mobile",description="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Enim voluptatibus vero quam obcaecati ipsa! Quaerat voluptatem ipsa, perferendis deserunt asperiores, repellat dolore incidunt vero atque ducimus rerum nostrum excepturi! Aperiam.",
#		coupon="FC100").save()
	return render_template('test.html',coupon=CouponCode.objects())

@app.route('/coupon/<string:uid>')
def detailView(uid):
	return render_template('detailedview.html')

@app.route('/alert')
def alertView():
	pass

@app.route('/submit-coupon')
def submitCoupon():
	pass

## 2. Admin Panel View  #########################
@app.route('/admin')
def adminPanel():
	pass

@app.route('/admin/new/<string:uid>')
def createCoupon(uid):
	pass

@app.route('/admin/edit/<string:uid>')
def editCoupon(uid):
	pass

@app.route('/admin/delete/<string:uid>')
def deleteCoupon(uid):
	pass



## 3. User accounts ##############################
@app.route('/login')
def signin():
	pass

@app.route('/logout')
def signout():
	pass

@app.route('/register')
def signup():
	pass

@app.route('/contact')
def contact():
	pass



###################################################
## Run the Code 
#####
if __name__=="__main__":
	app.run(debug=True,host='localhost',port=80)