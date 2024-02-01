from flask import Flask, render_template, url_for, flash, redirect
# import log forms from the form file
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

# function to fetch all info from the vehicle database
# vehicles = classes.vehicles.vehiclesDB.queryVehiclesGeneral()
app = Flask(__name__)
app.app_context().push() # gives the context to create the db from outside the application

# secret key for the app
app.config['SECRET_KEY'] = '3a91a34e53b72ed106d2bd8e87fe37ae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///driverAndTruck.db'

# Creates the database instance. We can represent the db structures as classes or models
db = SQLAlchemy(app)

# this class handles the user info in the db made for this purpose
class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True) # creates the column for the id
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    licenses = db.Column(db.String(120), unique=True, nullable=False)
    # image of the user
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # how the object is printed whenever we print it our
    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username, self.licenses, self.image_file)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/queryVehicles')
# def query():
#     return render_template('query.html', vehicles=vehicles)

# add the methods so the function will accept getting and sending information
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Create for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)