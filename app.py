from flask import Flask, json, url_for, request, render_template
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, create_engine
from geojson import Point, MultiPoint
import jinja2
from json import dumps
from pprint import pprint
from apidata import updateBTC, updateETH, updateDOGE
from tanner_scripts import tanner_btc, tanner_eth, tanner_doge
from cat_preds import buy_or_sell
import csv

app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/crypto.db'
# db = SQLAlchemy(app)
#This is a test comment to push for changes

# db.Model.metadata.reflect(db.engine)

# class Bitcoin(db.Model):
#     __tablename__ = 'btc'
#     __table_args__ = { 'extend_existing': True }
#     rowid = db.Column(db.Integer, primary_key=True)

# class Config(db.Model):
#     __tablename__ = 'config'
#     __table_args__ = { 'extend_existing': True }
#     rowid = db.Column(db.Integer, primary_key=True)

# class Ethereum(db.Model):
#     __tablename__ = 'eth'
#     __table_args__ = { 'extend_existing': True }
#     rowid = db.Column(db.Integer, primary_key=True)

# class Dogecoin(db.Model):
#     __tablename__ = 'doge'
#     __table_args__ = { 'extend_existing': True }
#     rowid = db.Column(db.Integer, primary_key=True)

# # Create an instance of Flask
# app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return render_template("index.html")

@app.route("/bitcoin")
def bitcoin():
    output = buy_or_sell('btc')
    updateBTC()
    tanner_btc()
    return render_template("bitcoin.html", output=output)


@app.route("/ethereum")
def ethereum():
    output = buy_or_sell('eth')
    updateETH()
    tanner_eth()
    return render_template("ethereum.html", output=output)

@app.route("/doge")
def dogecoin():
    output = buy_or_sell('doge')
    updateDOGE()
    tanner_doge()
    return render_template("doge.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
