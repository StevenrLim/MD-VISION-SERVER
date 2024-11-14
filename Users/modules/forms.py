from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import *



class newUserForm(FlaskForm):
    userID = StringField("User ID",validators=[DataRequired()])
    name = StringField("Name",validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
