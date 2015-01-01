import datetime
from app import db
# Notes
# ExpiryDate datetime.date(2014,12,20).strftime('%d%m%Y')  == 30122014
#
class CouponCode(db.Document):
	uid = StringField(required=True)
	date = DateTimeField(default=datetime.datetime.now,required=True)
	expirydate = DateTimeField(required=True)
	status = BooleanField(default=False)
	title = StringField(required=True)
	category = StringField(required=True)
	categoryid = IntField(required=False)
	subcategory = StringField(required=True)  # Prepaid | PostPaid | DTH 
	description = StringField(required=True)
	coupon = StringField(required=True)
	like = IntField()
	dislike = IntField()
	
#	def IsCouponExpired(date,expirydate):
#		if date.strftime('%d%m%Y') == expirydate.strftime('%d%m%Y'):
#			return True
#		else : 
#			return False

#	def buildURL(self.date,self.title):
#		return url_for('couponView', kwargs={"uid":self.uid,"title":self.title})


