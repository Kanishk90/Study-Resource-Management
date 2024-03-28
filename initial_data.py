from main import app
from application.models import db,Role

with app.app_context():
    db.create_all()
    admin = Role(id = 'admin',name = 'Admin',description = 'Admin description')
    db.session.add(admin)

    try:
        db.session.commit()
    except:
        pass