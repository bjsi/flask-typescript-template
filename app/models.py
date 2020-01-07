from app import db
import datetime as dt


# Simple example of a note database table

class Note(db.Model):

    """ A Note
    :id: Integer. Unique note id.
    :created_at: DateTime. When the note was created
    :content: Text. The note's content
    """

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow())
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Note: id={self.id}>"
