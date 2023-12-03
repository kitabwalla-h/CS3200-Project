from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


employees = Blueprint('employees', __name__)

# Get all employee info from the database
@employees.route('/employees', methods=['GET'])
def get_employees():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of employees
    cursor.execute('SELECT * FROM HuskyEatzEmployee')

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

# add new employees to database
@employees.route('/employees', methods=['POST'])
def add_new_employee():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variables
    first_name = the_data['FirstName']
    last_name = the_data['LastName']
    role = the_data['Role']
    employee_id = the_data['EmployeeID']

    # Constructing the query
    query = 'INSERT INTO HuskyEatzEmployee (FirstName, LastName, Role, EmployeeID) VALUES ("'
    query += first_name + '", "'
    query += last_name + '", "'
    query += role + '", '
    query += str(employee_id) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# update employee details
@employees.route('/employees/<EmployeeID>', methods=['PUT'])
def update_employee(employee_id):
    cursor = db.get_db().cursor()

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variables
    first_name = the_data['FirstName']
    last_name = the_data['LastName']
    role = the_data['Role']

    # constructing the query
    query = 'UPDATE HuskyEatzEmployee SET FirstName = %s, LastName = %s, Role = %s WHERE EmployeeID = %s'

    cursor.execute(query, (first_name, last_name, role, employee_id))
    db.get_db().commit()

    return 'Success!'
    
# Delete employee from the database
@employees.route('/employees/<EmployeeID>', methods=['DELETE'])
def delete_employee(employee_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to delete an employee
    query = 'DELETE FROM HuskyEatzEmployee WHERE EmployeeID = %s'
    cursor.execute(query, (employee_id))

    # commit changes to the database
    db.get_db().commit()

    return 'Success!'
