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
	
	#return render_template("notifications.html")
"""