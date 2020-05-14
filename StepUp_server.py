from flask import Flask, render_template, url_for,jsonify, request, Response
from jinja2 import StrictUndefined
import io
import requests
import json
from datetime import datetime, time
from time import sleep
#from twilio.rest import Client
#from twilio.twiml.messaging_response import MessagingResponse
import os

import cx_Oracle
import pandas as pdS
from pandas import ExcelFile
from pandas import ExcelWriter
from model import db, connect_to_db, User, InterventionCycle, Student, ProviderOrg, StudentGroup, CurrentIntervention
#from flask_debugtoolbar import DebugToolbarExtension
con_str = 'psnavigator/navigate@172.21.170.234/CA528'
con = cx_Oracle.connect(con_str)
c = con.cursor()
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
	user_type = request.form["user_type"]

   
	user = User.query.filter_by(email=email).first()

	if user:
		flash("You have already registered! Please log-in!")
		return redirect("/login") 

	else:    
		user = User(
			email=email,
			password=password,
			fname=fname,
			lname=lname,
			user_type = user_type, 
			organization=provider_organization
			)

	db.session.add(user)
	db.session.commit()

	session["user_id"] = user.user_id 
	return redirect("/student_groups")

@app.route("/login")
def login():

	email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if user.password != password:
        flash("Incorrect password")

    session["user_id"] = user.user_id
    session['logged_in'] = True
    flash("you are logged in")
    return render_template("/student_gropus")


@app.route("/student_groups")

def extract_student_fromSIS_fordb(): 

		"""extract student info from SIS and add to StepUp DB table, Student"""
		student = request.args.get('student')
		(firstname, lastname)= student.split(" ")
		
		#test with this info and then add all other student info for model
		query="""
		SELECT student_number,
		 last_name, 
		 first_name,
		 dob,
		 schoolID  
		FROM students  
		where first_name='""" + (firstname) + """ 'AND last_name='"""+(lastname)+"""'"""
		
		query_results=c.execute(query)
		#results = pd.read_sql(query,con)
		df=pd.DataFrame(results)
		#display student name, dob and school id for user to select
		#onclick, add to 
		#need to unpack df results to get info to look for student in Student table
		student=Student.query.filter_by(student_number = student_number,
										dob = dob)

		#need to unpack results to get info to add student
		if not student:
			student=Student(student_number = student_number,
										stu_fname = first_name,
										stu_lname = last_name,
										dob = dob,
										schoolid = schoolID)
			db.session.add(student)
			db.session.commit()


		return (results.to_json(orient='records'))	
	

def add_student_to_student_groups():
	"""user can add a student to an existing group or add a student to a new group"""
	student_in_group=StudentGroup.query.filter_by(student_number=student_number)
	#if not student_in_group in StudentGroup:
	#	group=Student()

def create_current_intervention():






	"""
	When user logs in - the code will query student groups associated with
	the user displaying data available for each student in a chart ie. number of sessions attended
	number of sessions missed, interventiont type, start date, end date.

	when the student name is clicked the browser opens up a tab specific to the student
	with graphics (?) and starting criteria, data collected durng intervention, end goal

	return render_template("student_groups.html")

"""
@app.route("/notifictions")
def notifications():
"""
	 boilerplate notifications that will be sent to relevant parties when
	1. student attends a session
	2. student misses a session
	3. student achieves goal
	4. student exits intervention without achieving goal
	5. other(?)
	

	return render_template("notifications.html")"""


if __name__ == "__main__":
	connect_to_db(app)
	app.run(host='127.0.0.1')





