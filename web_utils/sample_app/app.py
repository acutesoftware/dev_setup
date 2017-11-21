#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os



from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import abort
from flask import flash   
   
from flask_login import LoginManager   
from flask_login import UserMixin   
from flask_login import login_required
from flask_login import login_user
from werkzeug import check_password_hash, generate_password_hash


app = Flask(__name__)


YOUR_APP_MENU

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='12345yesreally'
))


###################### HELPER FUNCTIONS#################

def start_server():
    formatter = logging.Formatter(
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        
    handler = RotatingFileHandler('netdiary.log', maxBytes=200000, backupCount=1)  # causes issues when log size hit on Win32
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)


    if netdiary_WEB_VERSION == "DEV":
        print("WARNING - DEBUG MODE ACTIVE")
        app.debug = True	# TURN THIS OFF IN PRODUCTION
        app.run(threaded=True, host='0.0.0.0', port=5000)
    else:
        app.run(threaded=True, host='0.0.0.0', port=5000)  # FOR PROD
    

    
is_authenticated = False


def am_i_authenticated():
    try:
        if session['logged_in'] == True:
            return True
    except:
        pass
    return False
       
###################### ROUTING #########################
    
@app.route("/")
def page_home():
    #user = g.user
    return render_template('index.html', 
        submenu = get_sub_menu(),
        username = 'admin',
        logged_on='Y')


@app.route('/login', methods=['GET', 'POST'])
def login():
    flash('You were logged in (Not really - TODO, implement this)')
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('page_home'))

   

   
        
def get_sub_menu():

    return ['add','edit']

  
@app.route("/about")
def page_about():
    return render_template('about.html')


     
if __name__ == "__main__":
    start_server()
