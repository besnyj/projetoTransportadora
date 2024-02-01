# models(objects) for the db
from __main__ import db


# this class handles the user info in the db made for this purpose
class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True) # creates the column for the id
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    licenses = db.Column(db.String(120), unique=True, nullable=False)
    # image of the user
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    truckHistory = db.relationship('Truck', backref='author', lazy=True) # not related to Column, this will query the users' posts

    # how the object is printed whenever we print it our
    def __repr__(self):
        return "User('{}', '{}', '{}', '{}')".format(self.username, self.licenses, self.truckHistory, self.image_file)

# holds the posts
class Truck(db.Model):
    title = db.Column(db.String(100), nullable=False)
    lastMaintenance = db.Column(db.String(120), nullable=False)
    lastTripStart = db.Column(db.String(120), nullable=False)
    lastTripEnd = db.Column(db.String(120), nullable=False)
    truck_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Truck('{self.title}', '{self.lastMaintenance}', '{self.lastTripStart}', '{self.lastTripEnd}')"