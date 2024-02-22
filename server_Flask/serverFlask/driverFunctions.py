def drivers():
    if not current_user.is_authenticated:
        flash('Login needed to access the information', category='danger')
        return redirect(url_for('home'))

    drivers = Driver.query.all()
    driverPic = url_for('static', filename='driver_pics/')
    return render_template('drivers.html', drivers=drivers, driverPic=driverPic)