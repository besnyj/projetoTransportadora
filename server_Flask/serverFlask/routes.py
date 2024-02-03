from flask import Flask, render_template, url_for, flash, redirect
from serverFlask.forms import RegistrationForm, LoginForm
from serverFlask.models import User, Driver, Mechanic, Vehicle
from serverFlask import app, db, bcrypt


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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password='1234')
        db.session.add(user) # add user to the db
        db.session.commit() # save changes
        flash('Your account has been created! You are now able to log in', category='success')
        return redirect(url_for('login'))
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