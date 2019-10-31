# import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# creating an app
app=Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# calculating one year prior to the latest_date
last_year= dt.datetime.strptime(latest_date, '%Y-%m-%d')-dt.timedelta(days=365)
last_year

# Query to return the last date in the date
latest_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
latest_date

# Create our session (link) from Python to the DB
session = Session(engine)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

@app.route("/api/v1.0/precipitation")
def precipitation(): 
    session= Session(engine)
# Retrieve the last 12 months of precipitation data
    precip = session.query(Measurement.date, func.sum(Measurement.prcp)).\
                    filter(Measurement.date >= last_year).\
                    group_by(Measurement.date).all()

    session.close()

    all_precip = list(np.ravel(precip))
    
    return jsonify(all_precip) 


# Return a JSON list of stations
@app.route("/api/v1.0/stations")
def stations():
    session= Session(engine)
    station1= session.query(Measurement.station).all()

    session.close()

    all_stations = list(np.ravel(station1))

    return jsonify(all_stations)


# Return a JSON list of temperatures
@app.route("/api/v1.0/tobs")
def temp():
    session= Session(engine)
    temperature= session.query(Measurement.date, Measurement.tobs).\
                    filter(Measurement.date >= last_year).\
                    group_by(Measurement.date).all()
    session.close()

    all_temps = list(np.ravel(temperature))

    return jsonify(all_temps)


# start and end date query
@app.route("/api/v1.0/<start>")
def calc_temps(start_date, end_date):
    session= Session(engine)
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all() 

    session.close()



if __name__ == '__main__':
    app.run(debug=True)
