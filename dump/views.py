from main import app,db
from flask import render_template
from database import CouponCode

@app.route('/')
def index():
    return render_template('base.html', title="Snehesh")