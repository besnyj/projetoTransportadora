from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from serverFlask.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('password')])

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
    submit = SubmitField('Add Driver')

class MechanicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    lastMaintenancePerformed = StringField('Last Maintenance Date', validators=[DataRequired()])