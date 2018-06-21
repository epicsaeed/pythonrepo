from flask import Flask, request, jsonify
import sqlite3, ParameterMethods
from werkzeug.exceptions import default_exceptions

app = Flask(__name__)

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.errorhandler(404)
def handle_notfound_error(e):
    return jsonify(),404

@app.errorhandler(400)
def handle_unexpected_error(e):
    return jsonify(),400
 
#displays all products in the database
@app.route('/products/',methods=['GET'])
def api_all():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_products = cur.execute('SELECT * FROM data').fetchall()
    return jsonify(all_products)


#displays details of specific id, deletes a product, updates a product
@app.route('/products/<string:id>',methods=['POST','GET','DELETE'])
def api_product(id):

    #checks if the passed product ID is
    if ParameterMethods.check_id(id):
        pass
    else:
        return jsonify(),400

    #initiate database connection 
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    if request.method == 'GET':
        #displays details of passed product id
        result = cur.execute("SELECT * FROM data WHERE productid=?",(id,)).fetchall()
        if not result:
            return jsonify(),404
        else:
            return jsonify(result)
    elif request.method == 'POST':
        #updates details of passed product id
        payload = request.get_json()

        #checks if payload is empty, returns 400 if so
        if not payload:
            return jsonify(),400

        #sets up parameters
        name = payload.get('name')
        size = payload.get('size')
        color = payload.get('color')
        in_stock = payload.get('in_stock')

        #returns a 400 if no known parameters are given
        if not(name or size or color or in_stock):
            print("no known parameter given")
            return jsonify(),404

        #manipulates passed parameteres for updating 
        if name != None:
            if name == "" or name == " ":
                name = "N/A"
            query = "UPDATE data SET name =? WHERE productid=?"
            cur.execute(query,(name,id))
            conn.commit()

        if size != None:
            if size == "" or size == " ":
                size = "N/A"
            query = "UPDATE data SET size =? WHERE productid=?"
            cur.execute(query,(size,id))
            conn.commit()

        if color != None:
            if color == "" or color == " ":
                color = "N/A"
            query = "UPDATE data SET color =? WHERE productid=?"
            cur.execute(query,(color,id))
            conn.commit()

        if in_stock != None:
            if ParameterMethods.check_stock(in_stock):
                query = "UPDATE data SET instock =? WHERE productid=?"
                cur.execute(query,(in_stock,id))
                conn.commit()
            else:
                return jsonify(),404

        return jsonify(),200
    elif request.method == 'DELETE':
        #deletes item of passed product id

        #checks if the pid exists in DB and returns 404 if not
        cur.execute("SELECT * FROM data WHERE productid = ?",(id,))
        data = cur.fetchall()
        if len(data) == 0:
            return jsonify(), 404
        else:
            cur.execute("DELETE FROM data WHERE productid =?",(id,))
            conn.commit()
            return jsonify(),200
    else:
        #return NOT FOUND if mehtod is not of the above.
        return jsonify(),404

@app.route('/products/add',methods=['PUT'])
def api_add():
    payload = request.get_json()
    details = {"name":"","product_id":"","size":"","color":"","in_stock":""}

    if ParameterMethods.check_PUT_json(payload):
        pass
    else:
        return jsonify(),400

    if "product_id" in payload:
        pid = str(payload['product_id'])
        details["product_id"]=pid
        print(pid)
        if not pid.isdigit() or len(pid) != 7:
            return jsonify(),404
    else:
        return jsonify(),404

    if "in_stock" in payload:
        instock = str(payload['in_stock'])
        details["in_stock"]=instock
        if not instock.isdigit() or not instock:
            return jsonify(),404
    else:
        return jsonify(),404

    if "name" in payload:
        name = payload['name']
        if not name:
            name = "N/A"
    else:
        name = "N/A"
    
    if "size" in payload:
        size = payload['size']
        if not size:
            size = "N/A"
    else:
        size = "N/A"

    if "color" in payload:
        color = payload['color']
        if not color:
            color = "N/A"
    else:
        color = "N/A"

    details["name"]=name
    details["color"]=color
    details["size"]=size

    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    found = []
       #checks if the pid exists in DB and returns a conflict error status code
    cur.execute("SELECT * FROM data WHERE productid LIKE ?",(pid,))
    for row in cur.fetchall():
        found.append(row)
        if found:
            return jsonify(), 409

    cur.execute("INSERT INTO data VALUES(:productid,:name,:size,:color,:instock)",{'productid':pid,'name':name,'size':size,'color':color,'instock':instock})
    conn.commit()

    return jsonify(details),200

#allows user to search by id,name,size, and/or color
@app.route('/products/search')
def search():
    query_parameters = request.args

    #checks for inserted parameters 
    id = query_parameters.get('productid')
    name = query_parameters.get('name')
    size = query_parameters.get('size')
    color = query_parameters.get('color')
    
    query = "SELECT * FROM data WHERE"
    to_filter = []

    if id:
        query += ' productid LIKE ? AND'
        to_filter.append('%'+id+'%')
    if name:
        query += ' name LIKE ? AND'
        to_filter.append('%'+name+'%')
    if size:
        query += ' size LIKE ? AND'
        to_filter.append('%'+size+'%')
    if color:
        query += ' color LIKE ? AND'
        to_filter.append('%'+color+'%')
    if not (id or name or size or color):
        return jsonify(),404

    query = query[:-4]

    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query,to_filter).fetchall()
    return jsonify(results)

app.run(port=9214)

