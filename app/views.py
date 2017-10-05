from app import app, db
from flask import render_template
from models import *

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

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")