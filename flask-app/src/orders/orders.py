from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


orders = Blueprint('orders', __name__)

# Get all the orders given a specific vendor 
@orders.route('/orders/<vendor_id>', methods=['GET'])
def get_orders_by_vendor(vendor_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = 'SELECT * FROM Order WHERE VendorID = ' + str(vendor_id) + ' ;'
    cursor.execute(query)

    # grab the column headers from the returned data
    row_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the status of a specific order
@orders.route('/orders/<order_details_id>/status', methods=['GET'])
def get_order_status(order_details_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    query = 'SELECT * FROM OrderStatus WHERE OrderDetailsID =' + str(order_details_id) + ';'
    # use cursor to query the database for a list of products
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)