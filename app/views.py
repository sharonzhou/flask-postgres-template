from flask import render_template
from app import app, db
from app.models import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/db")
def add_to_db():
    thing = Thing()
    db.session.add(thing)
    db.session.commit()
    things = Thing.query.all()
    return render_template("db.html", things=things)