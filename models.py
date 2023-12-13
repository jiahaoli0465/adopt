"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://t4.ftcdn.net/jpg/01/99/00/79/360_F_199007925_NolyRdRrdYqUAGdVZV38P4WX8pYfBaRP.jpg"

db = SQLAlchemy()


class Pet(db.Model):
    """all pets table"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = False, default = GENERIC_IMAGE)

    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    def image_url(self):
        """Return image for pet -- bespoke or generic."""
        if self.photo_url == "":
            return GENERIC_IMAGE
        
        return self.photo_url or GENERIC_IMAGE
    
def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)