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
  goal = db.Column(db.string(64), nullable=False)
  intervention_type = db.Column(db.string(20), nullable=False)
  comment = db.Column(db.string(120), nullable=False)
  grade = db.Column(db.Integer, nullable=False)
  student_id = db.Column(db.integer,
                         db.ForeignKey(students.student_number)) # inline relationship (many-to-one)
  #provider = db.Column(db.string(100),
                      #   db.ForeignKey(providers.organization)) # one to one (one incident has one provider)

class Students(db.Model):
  """stores information of students receiving interventions"""
  __tablename__ = "students" 

  student_number = db.Column(db.Integer,
                            primary_key=True)
  stu_fname = db.Column(db.string(20), nullable=False)
  stu_lname = db.Column(db.string(20), nullable=False)
  previous_intervention = db.Column(db.integer,
                                    db.ForeignKey(cycles.intervention_id)) # one-to-many
  teacher = db.Colum(db.string(20), nullable=True)

class ProviderOrgs(db.Model):
  """stores information about intervention providers"""
  __tablename__ = "providers" 

  provider_id = db.Column(db.Integer,
                            autoincrement = True
                            primary_key=True)
  organization_name = db.Column(db.string(64), nullable=False)
  provider_email = db.Column(db.string(64), nullable=True)
  provider_phone = db.Column(db.integer, nullable=True)
  organization_phone = db.Column(db.string(20), nullable=False)



class StudentGroups(db.Model):
    """stores information about students in a group receiving the same intervnetion"""
  __tablename__ = "student_group"  
  group_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key=True)
  student_number = db.Column(db.integer,
                      db.ForeignKey(students.student_number))
  provider_id = db.Column(db.integer,
                      db.ForeignKey(providers.provider_id))
  group_name = db.Column(db.string(64), nullable = False)

class InterventionTypes(db.Model):
    __tablename__ = "intervention_type"

    type_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key=True)
    classification = db.Column(db.string(20), nullable=False) # pull down menu with predetermined labels and option for 'other'


class CurrentIntervention (db.Model):
    __tablename__ = "current_group"

    current_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key=True)
    intervention_id = db.Column(db.integer,
                      db.ForeignKey(cycles.intervention_id))
    formative_data = db.Column(db.float,
                                nullable=False)
    type_id = db.Column(db.integer,
                  db.ForeignKey(intervention_type.type_id))
    provider_id =db.Column(db.integer,
                          db.ForeignKey(providers.provider_id))
    group_id =db.Column(db.integer,
                                    db.ForeignKey(student_groups.group_id))





