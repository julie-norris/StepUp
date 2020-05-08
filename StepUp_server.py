from flask import Flask, render_template, url_for,jsonify, request, Response
from jinja2 import StrictUndefined
import io
import requests
import json
#import cx_Oracle
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
from flask_debugtoolbar import DebugToolbarExtension
#con_str = 'psnavigator/navigate@xxxxxxx/xxxx'
#con = cx_Oracle.connect(con_str)
#c = con.cursor()
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
"""login and/or register. users must be associated with an organization"""
@app.route("/")
def home():
	"""Homepage - log in/register here"""


	return render_template("home.html")
	
@app.route("/register_new_user")
def register():
	"""Creates a new user in the database."""

    provider_organization = request.form["provider_organization"]
    email = request.form["email"]
    password = request.form["password"]
    fname = request.form["fname"]
    lname = request.form["lname"]
    phone = request.form["phone_number"]
    

    #match = re.match(r'^[a-zA-Z0-9 -]{5,9}$', license_number)
"""
    #if not match:
    #    flash("Invalid license number. Try again.")
    #    return redirect("/register")

   """ user = Person.query.filter_by(email=email).first()

    if user:
        flash("You have already registered! Please log-in!")
        return redirect("/login")

    else:    
        user = Person(
            email=email,
            password=password,
            fname=fname,
            lname=lname,
            phone=phone, 
            organization=provider_organization
            )

    db.session.add(user)
    db.session.commit()

#  NEED SOMETHING HERE TO MAKE SURE THEY ARE LOGGED IN -- IS THIS ENOUGH:
    session["user_id"] = user.user_id 
    
    flash("Thank you for registering for CarPool! You have been logged in!")
    
    if driver_or_rider == 'driver':
        return redirect("/driver")
    else:
        return redirect("/rider")
"""
@app.route("/add_student")
def add_student(): 
	"""user can add a student to an existing group or add a student to a new group"""

	return render_template("add_student.html")

@app.route("/student_groups")
def student_groups():
	
	"""When user logs in - the code will query student groups associated with
	the user displaying data available for each student in a chart ie. number of sessions attended
	number of sessions missed, interventiont type, start date, end date."""

	"""when the student name is clicked the browser opens up a tab specific to the student
	with graphics (?) and starting criteria, data collected durng intervention, end goal"""

	return render_template("student_groups.html")


@app.route("/notifictions")
def notifications():

	""" boilerplate notifications that will be sent to relevant parties when
	1. student attends a session
	2. student misses a session
	3. student achieves goal
	4. student exits intervention without achieving goal
	5. other(?)
	"""

	return render_template("notifications.html")


if __name__ == "__main__":
    #connect_to_db(app)
    app.run(host='127.0.0.1')





