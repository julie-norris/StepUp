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





