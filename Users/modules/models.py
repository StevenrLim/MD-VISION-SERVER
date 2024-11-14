from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from global_model import db


class Users(db.Model):
    #__bind_key__ = "auth"
    #__tablename__ = 'auth_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    userID =  db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #Create a string
    def __repr__(self):
        return '<Name %r>' % self.name
    

