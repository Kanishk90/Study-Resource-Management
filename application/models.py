from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    pass    

class Role(db.Model):
    pass

class StudyResource(db.Model):
    pass
