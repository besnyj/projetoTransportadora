from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from serverFlask.models import User, Driver, Mechanic
from flask_wtf.file import FileRequired, FileField
from serverFlask import db


class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('password')])
    register_user_code = StringField('Register Code', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    # we can change the word and arg "field" to the filed we want to check like user or password
    # def validate_field(self, field):
    #     if True:
    #         raise ValidationError('Validation Message')

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is already in use. Please choose a different username')

    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('The email is already in use. Please choose a different valid email')


class LoginForm(FlaskForm):

    email = StringField('Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DriverForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    licenses = StringField('Licenses', validators=[DataRequired()])
    tripHistory = StringField('Trip History', [DataRequired()])
    file = FileField("File")
    submit = SubmitField('Register Driver')


class MechanicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    lastMaintenancePerformed = StringField('Last Maintenance Date', validators=[DataRequired()])
    file = FileField("File")
    submit = SubmitField('Register Mechanic')

class VehicleForm(FlaskForm):

    def driverIdLook(self):
        driver = Driver.query.filter_by(name=self).first()
        return driver.id

    def mechanicIdLook(self):
        mechanic = Mechanic.query.filter_by(name=self).first()
        return mechanic.id

    def driverNameLook(self):
        driver = Driver.query.filter_by(id=self).first()
        return driver.name

    def mechanicNameLook(self):
        mechanic = Mechanic.query.filter_by(id=self).first()
        return mechanic.name

    licensePlate = StringField('License Plate', validators=[DataRequired(),Length(max=8)])
    type = StringField('Type', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])
    lastMaintenance = StringField('Date of last maintenance', validators=[DataRequired()])
    driver_id = StringField("Assigned Driver's Name", validators=[DataRequired()])
    mechanic_id = StringField("Assigned Mechanic's Name", validators=[DataRequired()])
    extra = StringField("Extra", validators=[DataRequired()])
    submit = SubmitField('Register Vehicle')

class ParcelsForm(FlaskForm):
    driver_id = StringField("Assigned Driver's Name", validators=[DataRequired()])
    origin = StringField('Origin', validators=[DataRequired()])
    destiny = StringField('Destiny', validators=[DataRequired()])
    expectedArrDate = StringField('Expected Arrive Date', validators=[DataRequired()])
    submit = SubmitField('Submit Parcel for Delivery')

class TestForm(FlaskForm):
    file = FileField('Image', validators=[FileRequired()])
    submit = SubmitField('Upload')

class UpdateDriverForm(FlaskForm):
    age = StringField('Age', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    licenses = StringField('Licenses', validators=[DataRequired()])
    tripHistory = StringField('Trip History', [DataRequired()])
    file = FileField("File")
    submit = SubmitField('Update Driver')

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is already in use. Please choose a different username')

    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('The email is already in use. Please choose a different valid email')