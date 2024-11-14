from flask import *
from Users.modules.forms import *
from Users.modules.models import *

Users_bp = Blueprint("Users",__name__,template_folder="templates")

#Add New Auth User Route
@Users_bp.route('/add_user', methods=['GET','POST'])
def add_user():
    userID = None
    name = None
    password = None
    form = newUserForm()
    message_state = 0
    if form.validate_on_submit():
        user = Users.query.filter_by(userID=form.userID.data).first()
        if user is None:
            user = Users(name=form.name.data, userID=form.userID.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("User Added Successfully")
            return redirect(url_for("Users.user_list"))
        else:
            flash("UserID is not UNIQUE, user not successfully added")
            message_state = 1
        form.userID.data = ''
        form.name.data = ''
        form.password.data = ''
    our_users = Users.query.order_by(Users.date_added)
    return render_template("adding_user.html", userID = userID, name = name, password = password, form = form, our_users=our_users, message_state=message_state)        

#Modify User Route
@Users_bp.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = newUserForm()
    name_to_update = Users.query.get_or_404(id)
    form.userID.data = name_to_update.userID
    form.name.data = name_to_update.name
    form.password.data = name_to_update.password
    message_state = 0
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.password = request.form['password']
        try:
            db.session.commit()
            flash("User Updated Successfully")
            return redirect(url_for('Users.user_list'))
        except:
            flash("Error trying to Update")
            message_state = 1
            
    return render_template("update.html",form=form, name_to_update = name_to_update,message_state=message_state)

    


@Users_bp.route('/user_list', methods=['GET','POST'])
def user_list():
    our_users = Users.query.order_by(Users.date_added)
    return render_template("auth_user_list.html", our_users=our_users)


def search_user(user , word ):
    if (word is None):
        return False
    all = user.name + user.userID
    return word.lower() in all.lower()

@Users_bp.route('/search_user_', methods=['POST'])
def search_user_():
    users=Users.query.order_by(Users.date_added)
    searchword=request.form.get('search',None)
    matchusers=[user for user in users if search_user(user,searchword)]
    templ = """
            {% for user in users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>
                    <a href="{{ url_for('Users.update_patient', id=user.id) }}">{{ user.userID }}</a>
                </td>
                <td>{{ user.name }}</td>
            </tr>
            {% endfor %}
    """
    return render_template_string(templ,users=matchusers)
