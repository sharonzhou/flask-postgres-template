from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
