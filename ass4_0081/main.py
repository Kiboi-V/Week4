from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import leaflet
from flask import render_template,url_for,Flask,jsonify,request, redirect, session

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:0081@localhost/VK_Webmap"
db = SQLAlchemy(app)

class Town(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Numeric(10, 8), nullable=False)
    lng = db.Column(db.Numeric(11, 8), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    iso2 = db.Column(db.String(2), nullable=False)
    admin_name = db.Column(db.String(255), nullable=False)
    capital = db.Column(db.String(255), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    population_proper = db.Column(db.Integer, nullable=False)

@app.route("/")
def index():
    return render_template("index.html",title="Home")

@app.route("/map")
def homepage():
    return render_template("map.html",title="Towns")

@app.route("/towns")
def get_towns():
    towns = Town.query.all()
    return jsonify([{"city": t.city, "lat": t.lat, "lng": t.lng, "population": t.population} for t in towns])

if __name__ == "__main__":
    app.run(debug=True)
