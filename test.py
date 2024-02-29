from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, flash



def userAuthenticated(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Login needed to access the informaton', category='danger')
            return redirect(url_for('home'))

        return function(*args, **kwargs)

    return wrapper