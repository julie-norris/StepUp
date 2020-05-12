from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

class Users(db.Model):
	"""stores information to identify user"""
	__tablename__ = "users"

	user_id = db.Column(db.Integer,
											autoincrement = True
											primary_key = True) # auto-increment
	
	email = db.Column(db.string(64), nullable=False)
	user_type = db.Column(db.string(20), nullable=False)
	organization = db.Column(db.string(64), nullable=False)
	provider_id= db.Column(db.integer, db.ForeignKey(providers.provider_id))


class InterventionCycles (db.Model):
	"""stores all cycles of intervention provided to students"""
	__tablename__ = "cycles"


	intervention_id = db.Column(db.Integer,
															autoincrement = True
															primary_key = True)

	start_date = db.Column(db.DateTime, nullable=False)
	end_date = db.Column(db.DateTime, nullable=False)
	goal = db.Column(db.string(120), nullable=False)
	intervention_type = db.Column(db.string(20), nullable=False)
	goal = db.Column(db.string(240), nullable=True)
	summative_data = db.Column(db.numeric(6,2), nullable-False)
	comment = db.Column(db.string(120), nullable=False)
	grade_level = db.Column(db.Integer, nullable=False)
	student_id = db.Column(db.integer,
												 db.ForeignKey(students.student_number)) # inline relationship (many-to-one)


class Students(db.Model):
	"""stores information of students receiving interventions"""
	__tablename__ = "students" 

	student_number = db.Column(db.Integer,
														primary_key=True)
	stu_fname = db.Column(db.string(20), nullable=False)
	stu_lname = db.Column(db.string(20), nullable=False)
	previous_intervention = db.Column(db.integer,
																		db.ForeignKey(cycles.intervention_id)) # one-to-many
	gpa = db.column(db.float, nullable=True)
	schoolid = db.column(db.integer, nullable=False)
	teacher = db.Colum(db.string(20), nullable=True)
	guardian = db.Column(db.string(64), nullable=True)
	SchoolAdmin = db.Column(db.string(64), nullable=True)
	Student_email = db.Column(db.string(64), nullable=True)
	isSpEd = db.Column(db.string(5), nullable=True)
	isEL = db.Column(db.string(5), nullable=True)
	isHomeless = db.Column(db.string(5), nullable=True)
	isFosterYouth = db.Column(db.string(5), nullable=True)



class ProviderOrgs(db.Model):
	"""stores information about intervention providers"""
	__tablename__ = "providers" 

	provider_id = db.Column(db.Integer,
														autoincrement = True
														primary_key=True)
	organization_name = db.Column(db.string(64), nullable=False)
	provider_name  = db.Column(db.string(64), nullable=True)
	provider_email = db.Column(db.string(64), nullable=True)
	organization_phone = db.Column(db.string(20), nullable=False)



class StudentGroups(db.Model):
		"""stores information about students in a group receiving the same intervnetion"""
	__tablename__ = "student_group"  
	
	group_id = db.Column(db.Integer,
												autoincrement = True,
												primary_key=True)
	student_number = db.Column(db.integer,
											db.ForeignKey(students.student_number))
	group_current_intervention_id = db.Column(db.integer,
											db.ForeignKey(current_intervention.current_id))
	group_name = db.Column(db.string(64), nullable = True)


class CurrentIntervention (db.Model):
		__tablename__ = "current_intervention"

		current_id = db.Column(db.Integer,
												autoincrement = True,
												primary_key=True)
		current_intervention_id = db.Column(db.integer,
											db.ForeignKey(cycles.intervention_id))
		formative_data = db.Column(db.numeric(6,2),
																nullable=False)
		current_provider_id =db.Column(db.integer,
													db.ForeignKey(providers.provider_id))
		current_group_id =db.Column(db.integer,
													db.ForeignKey(student_groups.group_id))



#########################################################################
#Helper Functions

def connect_to_db(app, database_uri='postgresql:///mtss'):

		app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
		# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
		db.app = app
		db.init_app(app)

if __name__ == "__main__":

		from server import app
		connect_to_db(app)

		db.create_all()






