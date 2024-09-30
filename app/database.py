from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class APTActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    link = db.Column(db.String(200))

