from flask import Flask, json, url_for, request, render_template
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, create_engine
from geojson import Point, MultiPoint
import jinja2
from json import dumps
from pprint import pprint
from apidata import updateBTC, updateETH, updateDOGE
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/crypto.db'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Bitcoin(db.Model):
    __tablename__ = 'btc'
    __table_args__ = { 'extend_existing': True }
    rowid = db.Column(db.Integer, primary_key=True)

class Config(db.Model):
    __tablename__ = 'config'
    __table_args__ = { 'extend_existing': True }
    rowid = db.Column(db.Integer, primary_key=True)

class Ethereum(db.Model):
    __tablename__ = 'eth'
    __table_args__ = { 'extend_existing': True }
    rowid = db.Column(db.Integer, primary_key=True) 

class Dogecoin(db.Model):
    __tablename__ = 'doge'
    __table_args__ = { 'extend_existing': True }
    rowid = db.Column(db.Integer, primary_key=True)
 
# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/bitcoin<br/>"
        f"/ethereum<br/>"
        f"/dogecoin")

@app.route("/bitcoin")
def bitcoin():
    updateBTC()
    return render_template("btc.html")


# @app.route("/ethereum")
# def ethereum():
#     return render_template("")

@app.route("/dogecoin")
def dogecoin():
    updateDOGE()
    return render_template("doge.html")

if __name__ == "__main__":
    app.run(debug=True)



