from datetime import datetime
from global_model import db


# Creating Patient Class
class patients(db.Model):
    __bind_key__ = "patient"
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(200), nullable=False)
    l_name = db.Column(db.String(200), nullable=False)
    status= db.Column(db.String(200), nullable=False)
    date_mod = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_birth = db.Column(db.DateTime,nullable=False)
    med_notes = db.Column(db.Text,nullable=False)
    OHIP_num = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):
        return '<Name %r>' % self.name