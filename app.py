from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars
import os

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def scrape():
    mars_data=scrape_mars.scrape_info()
    mongo.db.update({}, mars_homework, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)