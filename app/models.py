from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    devices = db.relationship('Device', backref='device_user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name