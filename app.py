from flask import Flask, render_template, request
print(__file__)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myApp=Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(myApp)

class Admin(db.Model):
    name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(40), unique=True,nullable=False,)
    password = db.Column(db.String(40), unique=False, nullable=False)
    contact = db.Column(db.String(40), unique=True, nullable=False)

@myApp.route('/Dashboard', methods = ["POST"])
def mySignUp():
     if request.method == "POST" :
         admin = Admin()
         admin.name = request.form['name']
         admin.email = request.form['email']
         admin.password = request.form['pwd']
         admin.contact = request.form['tel']
         db.session.add(admin)
         db.session.commit()
         return render_template('Dashboard.html')



@myApp.route('/')
def index():
    return render_template('SignUp.html')
myApp.run()
