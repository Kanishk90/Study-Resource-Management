from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String(128))
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String(255),unique = True,nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    # study_resource = db.relationship('StudyResource',backref='creator')

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class StudyResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String,nullable=False)
    description = db.Column(db.String,nullable=False)
    # cretor_id = db.Column(db.Integer,db.ForeignKey('user_id'),nullable=False)
    resource_link = db.Column(db.String,nullable=False)
    is_approved = db.Column(db.Boolean,default = False)