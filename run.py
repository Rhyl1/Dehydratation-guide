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

"""This creates the app routes and functions, starting with the indexpage """
@app.route('/')
@app.route('/show_items')
def show_items():
    return render_template("items.html", items=mongo.db.items.find())

"""View created to add items to list"""
@app.route('/additems')
def add_items():
    return render_template("additems.html",
    types=mongo.db.types.find())

"""View specifies what happens after adding the items to list """
@app.route('/insert_item', methods=['POST'])
def insert_item():
    items = mongo.db.items
    items.insert_one(request.form.to_dict())
    return redirect(url_for('show_items'))

"""View created to edit items"""
@app.route('/edit_items')
def edit_preparations():
    return render_template("edit_all_items.html",
    items=mongo.db.items.find())

"""View created to edit individual items """
@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    the_item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    all_types = mongo.db.types.find()
    return render_template('edititem.html', item=the_item,
                           types=all_types)
"""Function specifies what happend after submitting edited individual items"""
@app.route('/update_item/<item_id>', methods=['POST'])
def update_item(item_id):
    items = mongo.db.items
    items.update({"_id": ObjectId(item_id)},
    {   'type_sort' : request.form.get('type_sort'),
        'description' : request.form.get('description'),
        'info' : request.form.get('info'),
        'hydra_temp' : request.form.get('hydra_temp'),
        'hydra_time_min' : request.form.get('hydra_time_min'),
        'hydra_time_max' : request.form.get('hydra_time_max'),
        'blanching' : request.form.get('blanching')
    })
    return redirect(url_for('show_items'))

"""Function specifies what happend after deleting individual items"""
@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    mongo.db.items.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('edit_preparations'))

"""View created to vieuw list of available preparation types"""
@app.route('/get_types')
def get_types():
    return render_template('types.html',
                           types=mongo.db.types.find())

"""View created to edit individual types"""
@app.route('/edit_type/<type_id>')
def edit_type(type_id):
    return render_template('edittype.html',
                           type=mongo.db.types.find_one(
                           {'_id': ObjectId(type_id)}))

"""Function specifies actions after editing individual types."""
@app.route('/update_type/<type_id>', methods=['POST'])
def update_type(type_id):
    mongo.db.types.update(
        {'_id': ObjectId(type_id)},
        {'type_sort': request.form.get('type_sort')})
    return redirect(url_for('get_types'))

"""Function specifies actions after deleting individual types."""
@app.route('/delete_type/<type_id>')
def delete_type(type_id):
    mongo.db.types.remove({'_id': ObjectId(type_id)})
    return redirect(url_for('get_types'))

"""View created to add type to list"""
@app.route('/addtypes')
def add_types():
    return render_template("addtypes.html",
    types=mongo.db.types.find())

"""View created to edit type from list of types"""
@app.route('/insert_type', methods=['POST'])
def insert_type():
    types = mongo.db.types
    types.insert_one(request.form.to_dict())
    return redirect(url_for('get_types'))

"""This sets the IP and Port host settings. When site needs to go into production, set debug value to false """

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)