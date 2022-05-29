from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/election_system'
#Posgress SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://siywiylmwgokkm:23fd8fafb3ba4a34db57ed7d41d59889b265de46618305e143c08cded1aa152a@ec2-44-195-169-163.compute-1.amazonaws.com/dfuvtrqao62433'
db = SQLAlchemy(app)
pwd = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "loginpage"
login_manager.login_message = "You are mot authorised to access this page. Please login first."
login_manager.login_message_category = "danger" 

from app import routes