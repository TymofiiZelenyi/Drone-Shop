import flask, flask_login
from flask_login import current_user

from .models import User

from Project.db import DATABASE
from Project.config_page import config_page

def logout():
    flask.session.clear()
    return flask.redirect('/')

@config_page(rule_name= 'registration.html')
def render_registration():
    message = ' '
    if flask.request.method == "POST":
        password = flask.request.form['password']
        conf_password = flask.request.form['conf_password']
        email= flask.request.form['email']
        # 
        db_email = User.query.filter_by(email = email).first()
        # 
        if password == conf_password:
            if db_email is None:
                user = User(
                    username= flask.request.form['username'],
                    email= email,
                    password= password
                )
                
                DATABASE.session.add(user)
                DATABASE.session.commit()
                message = "Регестрация успішно"
            else:
                message = "Користувач з таким email вже існує"
        else:
            message = 'Паролі не співпали'
            
    return {'message' : message}

def render_authorization():
    if flask.request.method == "POST":
        
        username_form = flask.request.form['username']
        password_form = flask.request.form['password']
        
        list_users = User.query.all()
        
        for user in list_users:
            if user.username == username_form and user.password == password_form:
                flask_login.login_user(user)
                
    if not current_user.is_authenticated:
        return flask.render_template(template_name_or_list= 'authorization.html')
    else:
        return flask.redirect('/')
