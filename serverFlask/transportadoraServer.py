from flask import Flask, render_template
import classes.vehicles.vehiclesDB


vehicles = classes.vehicles.vehiclesDB.queryVehiclesGeneral()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/query')
def query():
    return render_template('query.html', vehicles=vehicles)


if __name__=='__main__':
    app.run(debug=True)