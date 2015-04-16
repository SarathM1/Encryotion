from flask import Flask
from flask.ext.login import LoginManager, UserMixin, login_required,login_user,logout_user
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Email,Length
from flask import render_template,redirect,request,url_for,flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
app.secret_key = 'my secret key is this'

bootstrap = Bootstrap(app)

#dfa
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == 'POST':
        print 'done'
        fromDate=request.form['fromDate']
        fromHour=request.form['fromHour']
        fromMin=request.form['fromMin']

        print 'fromDate = '+ fromDate
        print 'fromHour = ' + fromHour
        print 'fromMinute = ' + fromMin
        return  render_template('Home.html',results=None)
    return  render_template('Home.html',results=None)
 

 
 
if __name__ == '__main__':
	app.run(port=5000,debug=True)
