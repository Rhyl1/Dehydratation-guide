import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

"""This specifies the path to the eviroment settings file needed for database connection"""

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
"""This specifies the database connection settings """
app.config["MONGO_DBNAME"] = 'Dehydra'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

"""This creates the app routes and functions """
@app.route('/')
@app.route('/show_items')
def show_items():
    return render_template("items.html", items=mongo.db.items.find())

@app.route('/additems')
def add_items():
    return render_template("additems.html",
    types=mongo.db.types.find())

@app.route('/insert_item', methods=['POST'])
def insert_item():
    items = mongo.db.items
    items.insert_one(request.form.to_dict())
    return redirect(url_for('show_items'))

"""This sets the IP and Port host settings """
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)