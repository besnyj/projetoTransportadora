from flask import Flask, render_template, url_for, flash, redirect
from serverFlask.forms import RegistrationForm, LoginForm, DriverForm, VehicleForm
from serverFlask.models import User, Driver, Mechanic, Vehicle
from serverFlask import app, db, bcrypt
from flask_login import login_user, current_user, logout_user

@app.route('/')
@app.route('/home') # home is the front page when not logged
def home():
    if current_user.is_authenticated:
        return redirect(url_for('logged'))
    return render_template('home.html', methods=['GET', 'POST'])

@app.route('/vehicles')
def vehicles():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))
    return render_template('vehicles.html')

@app.route('/mechanics')
def mechanics():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))
    return render_template('mechanics.html')

@app.route('/parcels')
def parcels():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))
    return render_template('parcels.html')

@app.route('/logged', methods=['GET', 'POST'])
def logged():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))
    user = User.query.filter_by(email=current_user.email).first()
    return render_template('logged.html', user=user)

@app.route('/drivers')
def drivers():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))
    drivers = Driver.query.all()
    return render_template('drivers.html', drivers=drivers)


# add the methods so the function will accept getting and sending information
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('logged'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user) # add user to the db
        db.session.commit() # save changes
        flash('Your account has been created! You are now able to log in', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('logged'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('logged'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/addDriver', methods=['GET', 'POST'])
def addDriver():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))
    form = DriverForm()
    if form.validate_on_submit():
        driver = Driver(name=form.name.data, age=form.age.data, salary=form.salary.data,
                        licenses=form.licenses.data, tripHistory=form.tripHistory.data)
        db.session.add(driver)
        db.session.commit()
        flash('Driver added to the Database', category='success')
        return redirect(url_for('logged'))
    return render_template('addDriver.html', form=form)

@app.route('/addVehicle', methods=['GET', 'POST'])
def addVehicle():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))

    form = VehicleForm()
    if form.validate_on_submit():
        vehicle = Vehicle(licensePlate=form.licensePlate.data, type=form.type.data,
                          year=form.year.data, weight=form.weight.data,
                          lastMaintenance=form.lastMaintenance.data, driver_id=VehicleForm.driverIdLook(form.driver_id.data),
                          mechanic_id=VehicleForm.mechanicIdLook(form.mechanic_id.data), extra=form.extra.data)
        db.session.add(vehicle)
        db.session.commit()
        return redirect(url_for('logged'))
    return render_template('addVehicle.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

