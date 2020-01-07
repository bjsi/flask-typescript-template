from flask import current_app as app
from flask import render_template
from app import db
from app.models import Note


@app.route('/')
def home():
    notes = (db
             .session
             .query(Note)
             .all())
    return render_template('home.html', notes=notes)
