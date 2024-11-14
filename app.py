from flask import *
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from dotenv import load_dotenv
import os

from flask_compress import Compress

#Defined Imports
#from modules.forms import newUserForm
#from modules.models import Users, db

from patient.patients import patient_bp
from Users.Users import Users_bp
from global_model import db


load_dotenv()
#print(os.getenv("FLASK_ENV"))

#Creating Flask Instance
app = Flask(__name__)
Compress(app)
app.config['SECRET_KEY'] = "G11_ROCKS"

#Add Databse
#Test SQLLITE
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:slim4212002@localhost/auth_users'
app.config['SQLALCHEMY_BINDS'] = {'patient':'mysql+pymysql://root:slim4212002@localhost/patients'}

#Initialize db

db.init_app(app)

#Register Blueprints
app.register_blueprint(patient_bp)
app.register_blueprint(Users_bp)

#Default Route/homepage
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/ping')
def ping():
    print("test")
    message = jsonify({"message":"idk"})
    json_data = message.get_data()
    print(json_data)
    json_size = len(json_data)
    print(json_size)
    return message, 200
#@app.route('/delete', methods=['POST'])
#def delete():






