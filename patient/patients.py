from flask import *
from patient.modules.forms import *
from patient.modules.models import *


patient_bp = Blueprint("patient",__name__, template_folder="templates")


#Patient Profile
@patient_bp.route('/profile/<int:id>', methods=['GET','POST'])
def profile(id):
    patient = patients.query.get_or_404(id)
    return render_template("patient_profile.html",patient=patient)

@patient_bp.route('/patient_list', methods=['GET','POST'])
def patient_list():
    our_patients = patients.query.order_by(patients.id)
    return render_template("patient_list.html", our_patients=our_patients)

#Modify User Route
@patient_bp.route('/update_patient/<int:id>', methods=['GET','POST'])
def update_patient(id):
    form = newPatientForm()
    patient_to_update = patients.query.get_or_404(id)
    form.f_name.data = patient_to_update.f_name
    form.l_name.data = patient_to_update.l_name
    form.status.data = patient_to_update.status
    form.date_birth.data = patient_to_update.date_birth
    form.med_notes.data = patient_to_update.med_notes
    form.OHIP_num.data = patient_to_update.OHIP_num
    message_state = 0
    if request.method == "POST":
        patient_to_update.f_name = request.form['f_name']
        patient_to_update.l_name = request.form['l_name']
        patient_to_update.status = request.form['status']
        patient_to_update.date_birth = request.form['date_birth']
        patient_to_update.med_notes = request.form['med_notes']
        try:
            db.session.commit()
            flash("Patient Updated Successfully")
            return redirect(url_for('patient_list'))
        except:
            flash("Error trying to Update")
            message_state = 1
            
    return render_template("update_patient.html",
                           form=form, 
                           patient_to_update = patient_to_update,
                           message_state=message_state)

@patient_bp.route('/add_patient',methods=['GET','POST'])
def add_patient():
    f_name = None
    l_name = None
    status = None
    date_birth = None
    med_notes = None
    OHIP_num = None
    form = newPatientForm()
    message_state = 0
    if form.validate_on_submit():
        patient = patients.query.filter_by(OHIP_num=form.OHIP_num.data).first()
        if patient is None:
            patient = patients(f_name=form.f_name.data, 
                         l_name=form.l_name.data,
                         status=form.status.data,
                         med_notes=form.med_notes.data,
                         OHIP_num=form.OHIP_num.data,
                         date_birth=form.date_birth.data)
            db.session.add(patient)
            db.session.commit()
            flash("User Added Successfully")
            return redirect(url_for("patient_list"))
        else:
            flash("OHIP Number is not UNIQUE, user not successfully added")
            message_state = 1
        form.f_name.data = ''
        form.l_name.data = ''
        form.status.data = ''
        form.date_birth.data = ''
        form.med_notes.data = ''
        form.OHIP_num.data = ''
    our_patients = patients.query.order_by(patients.data_created)
    return render_template("adding_patient.html", 
                           f_name = f_name, 
                           l_name = l_name, 
                           status = status,
                           date_birth = date_birth,
                           med_notes = med_notes,
                           OHIP_num = OHIP_num, 
                           form = form, 
                           our_patients=our_patients, 
                           message_state=message_state)  


def search_patient(patient , word ):
    if (word is None):
        return False
    all = patient.f_name + patient.l_name
    return word.lower() in all.lower()

@patient_bp.route('/search_patient_', methods=['POST'])
def search_patient_():
    patient=patients.query.order_by(patients.data_created)
    searchword=request.form.get('search',None)
    matchpatients=[patients for patients in patient if search_patient(patient,searchword)]
    templ = """
            {% for patient in patients %}
            <tr>
                <td>{{ patient.id }}</td>
                <td>
                    <a href="{{ url_for('update_patient', id=patient.id) }}">{{ patient.f_name }}</a>
                </td>d
                <td>{{ patient.l_name }}</td>
            </tr>
            {% endfor %}
    """
    return render_template_string(templ,patients=matchpatients)



