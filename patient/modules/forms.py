from wtforms import *
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

#Creating Patient Form
class newPatientForm(FlaskForm):
    f_name=  StringField("First Name", validators=[DataRequired()])
    l_name=  StringField("Last Name", validators=[DataRequired()])
    status=  SelectField('Status', choices=[("","Select an option"),("admitted","admitted"),("operating","In Operation"),("discharged","discharged")], validators=[DataRequired()])
    date_birth = DateField('Date of Birth',format='%Y-%m-%d')
    med_notes = TextAreaField('Medical Notes', validators=[DataRequired()])
    OHIP_num = StringField('OHIP Number',validators=[DataRequired()])
    submit = SubmitField("Submit")
