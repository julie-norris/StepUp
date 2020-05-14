from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ProviderOrg(db.Model):
	"""stores information about intervention providers"""
	__tablename__ = "providers" 

	provider_id = db.Column(db.Integer,
												autoincrement = True,
												primary_key=True)
	organization_name = db.Column(db.String(64), nullable=False)
	provider_name  = db.Column(db.String(64), nullable=True)
	provider_email = db.Column(db.String(64), nullable=True)
	organization_phone = db.Column(db.String(20), nullable=False)
	# realtionship established with provider; one provider could be realated to many users
	users = db.relationship("User", back_populates="provider")


class User(db.Model):
	"""stores information to identify user"""
	__tablename__ = "users"

	user_id = db.Column(db.Integer,
												autoincrement = True,
												primary_key=True)
	email = db.Column(db.String(64), nullable=False)
	password = db.Column(db.String(64), nullable=False)
	fname = db.Column(db.String(64), nullable=False)
	lname = db.Column(db.String(64), nullable=False)
	user_type = db.Column(db.String(20), nullable=False)
	organization = db.Column(db.String(64), nullable=False)
	id_provider= db.Column(db.Integer, 
								db.ForeignKey('providers.provider_id'))
	
	#establishing a many to one relationship; one provider could have relationship with many providers /
	#(ie. work at many schools)
	provider = db.relationship("Provider", back_populates="users")

class InterventionCycle (db.Model):
	"""stores all cycles of intervention provided to students"""
	__tablename__ = "cycles"


	intervention_id = db.Column(db.Integer,
												autoincrement = True,
												primary_key=True)

	start_date = db.Column(db.DateTime, nullable=False)
	end_date = db.Column(db.DateTime, nullable=False)
	goal = db.Column(db.String(120), nullable=False)
	intervention_type = db.Column(db.String(20), nullable=False)
	goal = db.Column(db.String(240), nullable=True)
	summative_data = db.Column(db.Numeric(6,2), nullable=False)
	comment = db.Column(db.String(120), nullable=False)
	grade_level = db.Column(db.Integer, nullable=False)
	student_id = db.Column(db.Integer,
												 db.ForeignKey('students.student_number')) # inline relationship (many-to-one)

class Student(db.Model):
	"""stores information of students receiving interventions"""
	__tablename__ = "students" 

	student_number = db.Column(db.Integer,
												primary_key=True)
	stu_fname = db.Column(db.String(20), nullable=False)
	stu_lname = db.Column(db.String(20), nullable=False)
	previous_intervention = db.Column(db.Integer,
																		db.ForeignKey('cycles.intervention_id')) # one-to-many
	gpa = db.Column(db.Numeric(6,2), nullable=True)
	schoolid = db.Column(db.Integer, nullable=False)
	teacher = db.Column(db.String(20), nullable=True)
	guardian = db.Column(db.String(64), nullable=True)
	SchoolAdmin = db.Column(db.String(64), nullable=True)
	Student_email = db.Column(db.String(64), nullable=True)
	isSpEd = db.Column(db.String(5), nullable=True)
	isEL = db.Column(db.String(5), nullable=True)
	isHomeless = db.Column(db.String(5), nullable=True)
	isFosterYouth = db.Column(db.String(5), nullable=True)



class StudentGroup(db.Model):
	"""stores information about students in a group receiving the same intervnetion"""
	__tablename__ = "student_groups"

	group_id = db.Column(db.Integer,
						autoincrement = True,
						primary_key=True)
	student_number = db.Column(db.Integer,
											db.ForeignKey('students.student_number'))
	group_current_intervention_id = db.Column(db.Integer,
											db.ForeignKey('current_interventions.current_id'))
	group_name = db.Column(db.String(64), nullable = True)


class CurrentIntervention (db.Model):
	__tablename__ = "current_interventions"

	current_id = db.Column(db.Integer,
												autoincrement = True,
												primary_key=True)
	current_intervention_id = db.Column(db.Integer,
											db.ForeignKey('cycles.intervention_id'))
	formative_data = db.Column(db.Numeric(6,2),
																nullable=False)
	current_provider_id =db.Column(db.Integer,
													db.ForeignKey('providers.provider_id'))
	current_group_id =db.Column(db.Integer,
													db.ForeignKey('student_groups.group_id'))



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






