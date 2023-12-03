from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


vendors = Blueprint('vendors', __name__)

# Get all the vendors from the database
@vendors.route('/vendors', methods=['GET'])
def get_products():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT * FROM Vendor')

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

# # get specific vendor details
# @vendors.route('/vendors/<vendor_id>', methods=['GET'])
# def get_vendor_detail (vendor_id):

#     query = 'SELECT * FROM Vendor WHERE VendorID = ' + str(vendor_id)
#     current_app.logger.info(query)

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)

# # get vendors under a specific vendor type
# @vendors.route('/vendors/<vendor_type>', methods=['GET'])
# def get_vendor_detail (vendor_type):

#     query = 'SELECT * FROM Vendor WHERE VendorType = ' + str(vendor_type)
#     current_app.logger.info(query)

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)

# # get vendors under a specific cuisine type
# @vendors.route('/vendors/<cuisine_type>', methods=['GET'])
# def get_vendor_detail (cuisine_type):

#     query = 'SELECT * FROM Vendor WHERE CuisineType = ' + str(cuisine_type)
#     current_app.logger.info(query)
    
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)
    

# # get the prices of menu items from a specific menu
# @vendors.route('/vendors/<vendor_id>/<menu_id>/prices')
# def get_menu_prices(vendor_id, menu_id):
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT mi.Name, mi.Price
#         FROM Vendor v
#         JOIN Menu m on v.VendorID = m.VendorID
#         JOIN MenuItems mi on mi.MenuID = m.MenuID
#         WHERE v.VendorID = ' + str(vendor_id) and m.MenuID = ' + str(menu_id)
#         ORDER BY mi.Price DESC
#     '''
#     cursor.execute(query)
#     # grab the column headers from the returned data
#     column_headers = [x[0] for x in cursor.description]

#     # create an empty dictionary object to use in 
#     # putting column headers together with data
#     json_data = []

#     # fetch all the data from the cursor
#     theData = cursor.fetchall()

#     # for each of the rows, zip the data elements together with
#     # the column headers. 
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))

#     return jsonify(json_data)

# # get the list menu items from a specific menu
# @vendors.route('/vendors/<vendor_id>/<menu_id>')
# def get_menu_from_vendor(vendor_id, menu_id):
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT mi.Name, mi.Price
#         FROM Vendor v
#         JOIN Menu m on v.VendorID = m.VendorID
#         JOIN MenuItems mi on mi.MenuID = m.MenuID
#         WHERE v.VendorID = ' + str(vendor_id) and m.MenuID = ' + str(menu_id)
#     '''
#     cursor.execute(query)
#     # grab the column headers from the returned data
#     column_headers = [x[0] for x in cursor.description]

#     # create an empty dictionary object to use in 
#     # putting column headers together with data
#     json_data = []

#     # fetch all the data from the cursor
#     theData = cursor.fetchall()

#     # for each of the rows, zip the data elements together with
#     # the column headers. 
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))

#     return jsonify(json_data)

# # # get the top 5 products from the database
# # @products.route('/mostExpensive')
# # def get_most_pop_products():
# #     cursor = db.get_db().cursor()
# #     query = '''
# #         SELECT product_code, product_name, list_price, reorder_level
# #         FROM products
# #         ORDER BY list_price DESC
# #         LIMIT 5
# #     '''
# #     cursor.execute(query)
# #     # grab the column headers from the returned data
# #     column_headers = [x[0] for x in cursor.description]

# #     # create an empty dictionary object to use in 
# #     # putting column headers together with data
# #     json_data = []

# #     # fetch all the data from the cursor
# #     theData = cursor.fetchall()

# #     # for each of the rows, zip the data elements together with
# #     # the column headers. 
# #     for row in theData:
# #         json_data.append(dict(zip(column_headers, row)))

# #     return jsonify(json_data)


# # @products.route('/tenMostExpensive', methods=['GET'])
# # def get_10_most_expensive_products():
    
# #     query = '''
# #         SELECT product_code, product_name, list_price, reorder_level
# #         FROM products
# #         ORDER BY list_price DESC
# #         LIMIT 10
# #     '''

# #     cursor = db.get_db().cursor()
# #     cursor.execute(query)

# #     column_headers = [x[0] for x in cursor.description]

# #     # create an empty dictionary object to use in 
# #     # putting column headers together with data
# #     json_data = []

# #     # fetch all the data from the cursor
# #     theData = cursor.fetchall()

# #     # for each of the rows, zip the data elements together with
# #     # the column headers. 
# #     for row in theData:
# #         json_data.append(dict(zip(column_headers, row)))
    
# #     return jsonify(json_data)

# @vendors.route('/vendor', methods=['POST'])
# def add_new_vendor():
    
#     # collecting data from the request object 
#     the_data = request.json
#     current_app.logger.info(the_data)

#     #extracting the variable
#     name = the_data['VendorName']
#     vendor_type = the_data['VendorType']
#     cuisine_type = the_data['CuisineType']
#     phone = the_data['Phone']
#     email = the_data['Email']
#     employee_id = the_data['EmployeeID']

#     # Constructing the query
#     query = 'insert into Vendor (VendorName, VendorType, CuisineType, Phone, Email, EmployeeID) values ("'
#     query += name + '", "'
#     query += vendor_type + '", "'
#     query += cuisine_type + '", '
#     query += phone + '", '
#     query += email + '", '
#     query += employee_id + '", '
#     current_app.logger.info(query)

#     # executing and committing the insert statement 
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     db.get_db().commit()
    
#     return 'Success!'

# # @products.route('/product', methods=['POST'])
# # def add_new_product():
    
# #     # collecting data from the request object 
# #     the_data = request.json
# #     current_app.logger.info(the_data)

# #     #extracting the variable
# #     name = the_data['product_name']
# #     description = the_data['product_description']
# #     price = the_data['product_price']
# #     category = the_data['product_category']

# #     # Constructing the query
# #     query = 'insert into products (product_name, description, category, list_price) values ("'
# #     query += name + '", "'
# #     query += description + '", "'
# #     query += category + '", '
# #     query += str(price) + ')'
# #     current_app.logger.info(query)

# #     # executing and committing the insert statement 
# #     cursor = db.get_db().cursor()
# #     cursor.execute(query)
# #     db.get_db().commit()
    
# #     return 'Success!'

# # ### Get all product categories
# # @products.route('/categories', methods = ['GET'])
# # def get_all_categories():
# #     query = '''
# #         SELECT DISTINCT category AS label, category as value
# #         FROM products
# #         WHERE category IS NOT NULL
# #         ORDER BY category
# #     '''

# #     cursor = db.get_db().cursor()
# #     cursor.execute(query)

# #     json_data = []
# #     # fetch all the column headers and then all the data from the cursor
# #     column_headers = [x[0] for x in cursor.description]
# #     theData = cursor.fetchall()
# #     # zip headers and data together into dictionary and then append to json data dict.
# #     for row in theData:
# #         json_data.append(dict(zip(column_headers, row)))
    
# #     return jsonify(json_data)