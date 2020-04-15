from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt

engine = create_engine("sqlite:///Instructions/Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    return """
            Welcome to the Climate App!
            </br>
            </br>
            Available Routes:
            <ol>
              <li>/api/v1.0/precipitation</li>
              <li>/api/v1.0/stations</li>
              <li>/api/v1.0/tobs</li>
              <li>/api/v1.0/start and /api/v1.0/start/end
            </ol>
    """

if __name__ == "__main__":
    app.run(debug = True)


