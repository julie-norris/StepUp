from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

class Users(db.Model):
  """stores information to identify user"""
  __tablename__ = "user"

  user_id = db.Column(db.Integer,
                      autoincrement = True
                      primary_key = True) # auto-increment
  fname = db.Column(db.string(15), nullable=False)
  lname = db.Column(db.string(15), nullable=False)
  email = db.Column(db.string(64), nullable=False)
  user_type = db.Column(db.string(20), nullable=False)


class Intervention_Cycles (db.Model):
  """stores all cycles of intervention provided to students"""
  __tablename__ = "cycles"


  intervention_id = db.Column(db.Integer,
                              autoincrement = True
                              primary_key = True)

  start_date = db.Column(db.DateTime, nullable=False)

  end_date = db.Column(db.DateTime, nullable=False)
  goal = db.Column(db.string(64), nullable=False)
  intervention_type = db.Column(db.string(20), nullable=False)
  comment = db.Column(db.string(64), nullable=False)
  grade = db.Column(db.Integer, nullable=False)
  student_id = db.Column(db.integer,
                         db.ForeignKey(students.student_number)) # inline relationship (many-to-one)
  provider = db.Column(db.string(100),
                         db.ForeignKey(providers.organization)) # one to one (one incident has one provider)

class Students(db.Model):
  """stores information of students receiving interventions"""
  __tablename__ = "students" 

  student_number = db.Column(db.Integer,
                            primary_key=True)
  stu_fname = db.Column(db.string(20), nullable=False)
  stu_lname = db.Column(db.string(20), nullable=False)
  previous_intervention = db.Column(db.integer,
                                    db.ForeignKey(cycles.intervention_id)) # one-to-many


class Provider_Orgs(db.Model):
  """stores information about intervention providers"""
  __tablename__ = "providers" 

  organization = db.Column(db.string(64), 
                            primary_key=True,
                            nullable=False)
  provider_name = db.Column(db.string(64), nullable=False)
  provider_email = db.Column(db.string(64), nullable=False)
  provider_phone = db.Column(db.integer, nullable=False)
