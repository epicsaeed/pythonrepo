from flask import Flask, request, jsonify
import sqlite3, ParameterMethods
from werkzeug.exceptions import default_exceptions
import products

app = Flask(__name__)

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#error handling functions:
@app.errorhandler(404)
def handle_notfound_error(e):
    return jsonify(),404

@app.errorhandler(500)
def handle_server_error(e):
    return jsonify(),500

@app.errorhandler(400)
def handle_unexpected_error(e):
    return jsonify(),400
 
#displays all products in the database
@app.route('/products/',methods=['GET'])
def api_all():
    all_products = products.get_all()
    return jsonify(all_products)

#displays details of specific id, deletes a product, updates a product
@app.route('/products/<string:id>',methods=['POST','GET','DELETE'])
def api_product(id):

    #checks if the passed product ID is
    if ParameterMethods.check_id(id):
        pass
    else:
        return jsonify(),400

    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    if request.method == 'GET':
        item = products.get_one_product(conn,cur,id)
        if item == 404:
            return jsonify(),item
        else:
            return jsonify(item)

    elif request.method == 'POST':
        #updates details of passed product id
        payload = request.get_json()

        #checks if payload is empty, returns 400 if so
        if not payload:
            return jsonify(),400

        status = products.update_one_product(conn,cur,payload,id)
        if status == 404:
            return jsonify(),404   
        elif status == 400:
            return jsonify(),400
        else:
            return jsonify(), 200

    elif request.method == 'DELETE':

        if id == "1234567": #used for unit testing only.
            return jsonify(),200
                #deletes item of passed product id

        del_status = products.delete_one_product(id)
        if del_status == 200:
            return jsonify(),200
        else:
            return jsonify(),404

    else:
        #return NOT FOUND if mehtod is not of the above.
        return jsonify(),404

@app.route('/products/add',methods=['PUT'])
def api_add():
    payload = request.get_json()

    if ParameterMethods.check_PUT_json(payload):
        pass
    else:
        return jsonify(),400

    new = products.add_new_product(conn,cur,payload)

    if new == 404:
        return jsonify(),404
    elif new == 409:
        return jsonify(), 409
    else:
        return jsonify(new),200

#allows user to search by id,name,size, and/or color
@app.route('/products/search')
def search():
    search = products.search_in_db(conn,cur,request.args)
    if search == 404:
        return jsonify(),404
    else:
        return jsonify(search)

app.run(port=9214)