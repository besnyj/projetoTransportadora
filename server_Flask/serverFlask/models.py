# models are objects to input in the database
from serverFlask import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# this class handles the user info in the db made for this purpose
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)


class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(60), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    vehiclesAssigned = db.relationship('Vehicle', backref='driver', lazy=True)
    licenses = db.Column(db.String(120), nullable=True)
    tripHistory = db.Column(db.String(60), nullable=True)

    # how the object is printed whenever we print it our
    def __repr__(self):
        return f"Driver({self.id}, {self.username}, {self.email}, {self.password}, {self.name}, {self.age}, {self.role}, {self.salary}, {self.vehiclesAssigned}, {self.licenses}, {self.tripHistory}, {self.image_file})"

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(60), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    vehiclesAssigned = db.relationship('Vehicle', backref='mechanic', lazy=True)
    lastMaintenancePerformed = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"Mechanic({self.id}, {self.username}, {self.email}, {self.password}, {self.name}, {self.age}, {self.role}, {self.salary}, {self.vehiclesAssigned}, {self.lastMaintenancePerformed}, {self.image_file})"


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    licensePlate = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    lastMaintenance = db.Column(db.String(120), nullable=False)
    extra = db.Column(db.String(120), nullable=False)
    # assigns the vehicle to a specific driver and mechanic from the Driver, Mechanic tables with their unique id
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return (f"Vehicle({self.id}, {self.licensePlate}, {self.type}, {self.year}, {self.weight}, {self.lastMaintenance}, {self.extra}, {self.image_file})")