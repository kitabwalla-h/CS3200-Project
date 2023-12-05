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
    query = 'SELECT * FROM `Order` WHERE VendorID = ' + str(vendor_id) + ' ;'
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

#POST
#add new order
@orders.route('/orders', methods = ['POST'])
def add_new_order():
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    total = the_data['TotalSale']
    vendor = the_data['VendorID']
    date = the_data['DeliveryDate']
    customer = the_data['CustomerID']
    delivery = the_data['DeliveryPersonID']

    # Constructing the query
    query = 'insert into `Order` (TotalSale, VendorID, DeliveryDate, CustomerID, DeliveryPersonID) values ("{}", "{}", "{}", "{}", "{}");'.format(total, vendor, date, customer, delivery)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


#PUT
#update order 
@orders.route('/orders/<OrderID>', methods=['PUT'])
def update_customer(OrderID):
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    #extracting the variable
    total = the_data['TotalSale']
    vendor = the_data['VendorID']
    date = the_data['DeliveryDate']
    customer = the_data['CustomerID']
    delivery = the_data['DeliveryPersonID']

    # Constructing the query
    query = 'update `Order` SET TotalSale = "{}", VendorID = "{}",  DeliveryDate = "{}", CustomerID = "{}", DeliveryPersonID = "{}";'.format(total, vendor, date, customer, delivery)

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'



#DELETE
#remove an order 
@orders.route('/orders/<OrderID>', methods=['DELETE'])
def delete_order(OrderID):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM `Order` WHERE OrderID = ' + str(OrderID) + ';')
    db.get_db().commit()
    return 'Success!'

 #add new order
@orders.route('/orders/menuitems', methods = ['POST'])
def add_new_order_menuitesm():
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    orderdetailsid = the_data['OrderDetailsID']
    menuitemname = the_data['MenuItemName']

    # Constructing the query
    query = 'insert into MenuItemsInOrder (OrderDetailsID, MenuItemName) values ("{}", "{}");'.format(orderdetailsid, menuitemname)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@orders.route('/orders/pending/<vendor_id>', methods=['GET'])
def get_order_status(vendor_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = 'SELECT o.OrderID, o.VendorID, o.CustomerID, o.DeliveryPersonID, os.Status FROM `Order` o JOIN OrderDetails od on o.OrderID = od.OrderID'
    query = query + ' JOIN OrderStatus os on od.OrderDetailsID = os.OrderDetailsID'
    query = query + ' WHERE (o.VendorID = ' + str(vendor_id)
    query = query + ' AND os.Status = "pending");'

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


