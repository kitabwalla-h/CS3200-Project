from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


customers = Blueprint('customers', __name__)

# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Customer')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@customers.route('/customers/<CustomerID>', methods=['GET'])
def get_customer(CustomerID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Customer where CustomerID = {0}'.format(CustomerID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customers.route('/customers', methods=['POST'])
def add_new_customer():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    first_name = the_data['first_name']
    last_name = the_data['last_name']
    phone = the_data['phone']
    email = the_data['email']

    # Constructing the query
    query = 'insert into Customer (FirstName, LastName, Phone, Email) values ("'
    query += first_name + '", "'
    query += last_name + '", "'
    query += phone + '", "'
    query += email + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@customers.route('/customers/<CustomerID>', methods=['PUT'])
def update_customer(CustomerID):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    first_name = the_data['first_name']
    last_name = the_data['last_name']
    phone = the_data['phone']
    email = the_data['email']
    

    # Constructing the query
    query = 'update Customer SET '
    query += 'FirstName = "' + first_name + '", '
    query += 'LastName = "' + last_name + '", '
    query += 'Phone = " ' + phone + '", '
    query += 'Email = "' + email + '" WHERE CustomerID = ' + str(CustomerID) + ';' 
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@customers.route('/customers/<CustomerID>', methods=['DELETE'])
def delete_customer(CustomerID):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Customer WHERE CustomerID = ' + str(CustomerID) + ';')
    db.get_db().commit()
    return 'Success!'


# getting customer location
@customers.route('/customers/get-location/<CustomerID>', methods=['GET'])
def get_customer_location(CustomerID):
    cursor = db.get_db().cursor()
    cursor.execute('Select * from CustomerLocations where CustomerID = ' + str(CustomerID) + ';')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# updating customer location
@customers.route('/customers/update-location/<CustomerID>', methods=['PUT'])
def update_customer_location(CustomerID):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    street = the_data['Street']
    city = the_data['City']
    state = the_data['State']
    zipcode = the_data['ZipCode']

    # Constructing the query
    query = 'update CustomerLocations SET '
    query += 'Street = "' + street + '", '
    query += 'City = "' + city + '", '
    query += 'State = " ' + state + '", '
    query += 'ZipCode = "' + zipcode + '" WHERE CustomerID = ' + str(CustomerID) + ';' 
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
