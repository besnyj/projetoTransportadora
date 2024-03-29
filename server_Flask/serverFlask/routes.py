import os
import sqlite3

from flask import Flask, render_template, url_for, flash, redirect, request
from serverFlask.forms import (RegistrationForm, LoginForm, DriverForm, VehicleForm, MechanicForm,
                               ParcelsForm, TestForm, UpdateDriverForm, UpdateMechanicForm,
                               UpdateVehicleForm)
from serverFlask.models import User, Driver, Mechanic, Vehicle, ParcelsModel, Notes
from serverFlask import app, db, bcrypt, register_user_code
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from serverFlask.tools import userAuthenticated

@app.route('/')
@app.route('/home') # home is the front page when not logged
def home():
    if current_user.is_authenticated:
        return redirect(url_for('logged'))
    return render_template('home.html', methods=['GET', 'POST'])

@app.route('/vehicles', methods=['GET', 'POST'])
@userAuthenticated # decorator that redirects to the home page if user is not logged
def vehicles():
    vehicle = Vehicle.query.all()
    return render_template('vehicles.html', vehicles=vehicle)

@app.route('/drivers', methods=['GET', 'POST'])
@userAuthenticated
def drivers():

    drivers = Driver.query.all()
    driverPic = url_for('static', filename='driver_pics/')
    return render_template('drivers.html', drivers=drivers, driverPic=driverPic)

@app.route('/mechanics')
@userAuthenticated
def mechanics():

    mechanics = Mechanic.query.all()
    mechanicPic = url_for('static', filename='mechanic_pics/')
    return render_template('mechanics.html', mechanics=mechanics, mechanicPic=mechanicPic)

@app.route('/parcels')
@userAuthenticated
def parcels():
    parcels = ParcelsModel.query.all()
    return render_template('parcels.html', parcels=parcels)

@app.route('/updatevehicle', methods=['GET', 'POST'])
@userAuthenticated
def updatevehicle():

    vehicleRequest = request.args.get('vehicle')
    vehicle = Vehicle.query.filter_by(licensePlate=vehicleRequest).first()

    form = UpdateVehicleForm()

    if form.validate_on_submit():

        if form.lastMaintenance.data=="":
            vehicle.lastMaintenance = vehicle.lastMaintenance
        else:
            vehicle.lastMaintenance = form.lastMaintenance.data

        if form.extra.data=="":
            vehicle.extra=vehicle.extra
        else:
            vehicle.extra=form.extra.data

        if form.driverName.data=="":
            vehicle.driver_id=vehicle.driver_id
        else:
            driver = Driver.query.filter_by(name=form.driverName.data).first()
            vehicle.driver_id = driver.id
            vehicle.driverName = driver.name

        if form.mechanicName.data=="":
            vehicle.mechanic_id=vehicle.mechanic_id
        else:
            mechanic = Mechanic.query.filter_by(name=form.mechanicName.data).first()
            vehicle.mechanic_id=mechanic.id
            vehicle.mechanicName=mechanic.name

        db.session.commit()
        flash("Vehicle's information successfully updated", category='success')
        return redirect(url_for('vehicles'))
    return render_template('updatevehicle.html', vehicle=vehicle, form=form)

@app.route('/deletevehicle')
@userAuthenticated
def deletevehicle():

    vehicleRequest = request.args.get('vehicle')
    vehicle = Vehicle.query.filter_by(licensePlate=vehicleRequest).first()

    db.session.delete(vehicle)
    db.session.commit()
    flash('Vehicle successfully deleted from database', category='success')
    return redirect(url_for('vehicles'))

@app.route('/updatedriver', methods=['GET', 'POST'])
@userAuthenticated
def updatedriver():

    driverRequest = request.args.get('driver')
    driver = Driver.query.filter_by(name=driverRequest).first()

    form = UpdateDriverForm()
    if form.validate_on_submit():
        if form.age.data=="":
            driver.age=driver.age
        else:
            driver.age=form.age.data

        if form.salary.data=="":
            driver.salary=driver.salary
        else:
            driver.salary=form.salary.data

        if form.licenses.data=="":
            driver.licenses=driver.licenses
        else:
            driver.licenses=form.licenses.data

        if form.tripHistory.data=="":
            driver.tripHistory=driver.tripHistory
        else:
            driver.tripHistory=form.tripHistory.data

        if form.age.data=="":
            driver.age=driver.age
        else:
            driver.age=form.age.data

        db.session.commit()
        flash("Driver's information successfully updated", category='success')
        return redirect(url_for('drivers'))

    return render_template('updatedriver.html', driver=driver, form=form)

@app.route('/updatemechanic', methods=['GET', 'POST'])
@userAuthenticated
def updatemechanic():

    mechanicRequest = request.args.get('mechanic')
    mechanic = Mechanic.query.filter_by(name=mechanicRequest).first()

    form = UpdateMechanicForm()
    if form.validate_on_submit():

        if form.age.data=="":
            mechanic.age = mechanic.age
        else:
            mechanic.age = form.age.data

        if form.salary.data=="":
            mechanic.salary = mechanic.salary
        else:
            mechanic.salary = form.salary.data

        if form.role.data=="":
            mechanic.role = mechanic.role
        else:
            mechanic.role = form.role.data

        if form.lastMaintenance.data=="":
            mechanic.lastMaintenancePerformed = mechanic.lastMaintenancePerformed
        else:
            mechanic.lastMaintenancePerformed = form.lastMaintenance.data

        db.session.commit()
        flash("Mechanic's information successfully updated", category='success')
        return redirect(url_for('mechanics'))

    return render_template('updatemechanic.html', mechanic=mechanic, form=form)

@app.route('/logged', methods=['GET', 'POST'])
@userAuthenticated
def logged():
    user = User.query.filter_by(email=current_user.email).first()
    notes = Notes.query.all()
    drivers = Driver.query.all()
    mechanics = Mechanic.query.all()
    vehicles = Vehicle.query.all()
    return render_template('logged.html', user=user,
                           notes=notes, drivers=drivers, mechanics=mechanics,
                           vehicles=vehicles)

@app.route('/driverprofile', methods=['GET', 'POST'])
@userAuthenticated
def driverprofile():

    driverRequest = request.args.get('driver')
    driver = Driver.query.filter_by(name=driverRequest).first()
    driverPic = url_for('static', filename='driver_pics/')

    return render_template('driverprofile.html', driver=driver, driverPic=driverPic)

@app.route('/deletemechanic')
@userAuthenticated
def deletemechanic():
    mechanicRequest = request.args.get('mechanic')
    mechanic = Mechanic.query.filter_by(name=mechanicRequest).first()

    try:
        db.session.delete(mechanic)
        db.session.commit()
        flash('Mechanic successfully deleted from database', category='success')
        return redirect(url_for('mechanics'))
    except IntegrityError:
        db.session.rollback()
        flash(f"Please, designate a new mechanic for vehicles {mechanic.vehiclesAssigned} before deleting {mechanic.name}", category='danger')
        return redirect(url_for('mechanics'))

@app.route('/mechanicprofile')
@userAuthenticated
def mechanicprofile():

    mechanicRequest = request.args.get('mechanic')
    mechanic = Mechanic.query.filter_by(name=mechanicRequest).first()

    mechanicPic = url_for('static', filename='mechanic_pics/')

    return render_template('mechanicprofile.html', mechanic=mechanic, mechanicPic=mechanicPic)


@app.route('/deletedriver')
@userAuthenticated
def deletedriver():
    driverRequest = request.args.get('driver')
    driver = Driver.query.filter_by(name=driverRequest).first()

    try:
        db.session.delete(driver)
        db.session.commit()
        flash('Driver successfully deleted from database', category='success')
        return redirect(url_for('drivers'))
    except IntegrityError:
        db.session.rollback()
        flash(f"Please, designate a new mechanic for vehicles {driver.vehiclesAssigned} before deleting {driver.name}", category='danger')
        return redirect(url_for('drivers'))

# add the methods so the function will accept getting and sending information
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('logged'))
    form = RegistrationForm()
    if form.validate_on_submit() and form.register_user_code.data == register_user_code:
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
@userAuthenticated
def addDriver():
    form = DriverForm()
    if form.validate_on_submit():
        driver = Driver(name=form.name.data, age=form.age.data, salary=form.salary.data,
                        licenses=form.licenses.data, tripHistory=form.tripHistory.data)
        db.session.add(driver)
        db.session.commit()
        driver = Driver.query.filter_by(id=driver.id).first()
        driver.image_file = f'{driver.id}.png'
        db.session.commit()

        # saves the profile pic for the driver
        file = form.file.data
        file.filename = f'{driver.id}.png'
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{app.config['UPLOAD_FOLDER']}/driver_pics', secure_filename(file.filename)))


        flash('Driver added to the Database', category='success')
        return redirect(url_for('drivers'))
    return render_template('addDriver.html', form=form)

@app.route('/addVehicle', methods=['GET', 'POST'])
@userAuthenticated
def addVehicle():

    form = VehicleForm()
    if form.validate_on_submit():
            driver_id = VehicleForm.driverIdLook(form.driver_id.data)
            driverInfo = Driver.query.filter_by(id=driver_id).first()
            driver_name = driverInfo.name
            mechanic_id = VehicleForm.mechanicIdLook(form.mechanic_id.data)
            mechanicInfo = Mechanic.query.filter_by(id=mechanic_id).first()
            mechanic_name = mechanicInfo.name
            vehicle = Vehicle(licensePlate=form.licensePlate.data, type=form.type.data,
                              year=form.year.data, weight=form.weight.data,
                              lastMaintenance=form.lastMaintenance.data, driver_id=VehicleForm.driverIdLook(form.driver_id.data),
                              mechanic_id=VehicleForm.mechanicIdLook(form.mechanic_id.data), extra=form.extra.data,
                              driverName=driver_name, mechanicName=mechanic_name)
            db.session.add(vehicle)
            db.session.commit()
            return redirect(url_for('logged'))
            flash('Invalid Driver/Mechanic ID. Please, try again with valid IDs', category='danger')
            return redirect(url_for('addVehicle'))
    return render_template('addVehicle.html', form=form)

@app.route('/addMechanic', methods=['GET', 'POST'])
@userAuthenticated
def addMechanic():
    form = MechanicForm()
    if form.validate_on_submit():
        mechanic = Mechanic(name=form.name.data, age=form.age.data,
                            salary=form.salary.data, role=form.role.data,
                            lastMaintenancePerformed=form.lastMaintenancePerformed.data)
        db.session.add(mechanic)
        db.session.commit()
        mechanic = Mechanic.query.filter_by(id=mechanic.id).first()
        mechanic.image_file = f'{mechanic.id}.png'
        db.session.commit()

        file = form.file.data
        file.filename = f'{mechanic.id}.png'
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{app.config['UPLOAD_FOLDER']}/mechanic_pics', secure_filename(file.filename)))

        flash('Mechanic added to the Database', category='success')
        return redirect(url_for('mechanics'))
    return render_template('addMechanic.html', form=form)

@app.route('/addParcels', methods=['GET', 'POST'])
@userAuthenticated
def addParcels():

    form = ParcelsForm()
    if form.validate_on_submit():
        driver_id = VehicleForm.driverIdLook(form.driver_id.data)
        driverInfo = Driver.query.filter_by(id=driver_id).first()
        driver_name = driverInfo.name
        parcel = ParcelsModel(driver_id=driver_name, origin=form.origin.data,
                         destiny=form.destiny.data, expectedArrDate=form.expectedArrDate.data)
        db.session.add(parcel)
        db.session.commit()
        return redirect(url_for('parcels'))
        flash('Parcel added to the Database', category='success')
    return render_template('addParcels.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('login2.html')


