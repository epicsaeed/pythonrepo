from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

#returns a 404 HTTP status code 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#routes to the home page of the server
@app.route('/',methods=['GET'])
def main():
    return "<h1>Inventory App</h1><p>This is a web server for inventory.</p>"

#displays all products in the database
@app.route('/products',methods=['GET'])
def api_all():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_products = cur.execute('SELECT * FROM data').fetchall()
    return jsonify(all_products)

@app.route('/products/<int:id>',methods=['POST','GET'])
def api_product(id):
    if request.method == 'GET':

        query = "SELECT * FROM data WHERE productid=%s;"%id

        conn = sqlite3.connect('inventory.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        result = cur.execute(query).fetchall()
        
        if not result:
            return page_not_found(404)
        else:
            return jsonify(result)
    else:
        
        payload = request.get_json()
        to_filter = []

        #UPDATE data SET name AND
        query = "UPDATE data SET"


        if 'name' in payload:
            query+= ' name=? AND'
            to_filter.append(payload['name'])

        if 'size' in payload:
            query+= ' size=? AND'
            to_filter.append(payload['size'])

        if 'color' in payload:
            query+= ' color=? AND'
            to_filter.append(payload['color'])

        if 'in_stock' in payload:
            query+= ' instock=? AND'
            to_filter.append(payload['in_stock'])
        
        if ('name' and 'size' and 'color' and 'in_stock') not in payload:
            return page_not_found(404)

        query = query[:-4] + ' WHERE productid=?'

        to_filter.append(id)
        print(query)
        print(to_filter)
        return "Product has been updated", 200

        # conn = sqlite3.connect('inventory.db')
        # cur = conn.cursor()
        # cur.execute(query,to_filter)





@app.route('/products/add',methods=['PUT'])
def api_add():
    payload = request.get_json()

    pid = payload['product_id']
    name = payload['name']
    size = payload['size']
    color = payload['color']
    instock = payload['in_stock']

    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(:productid,:name,:size,:color,:instock)",{'productid':pid,'name':name,'size':size,'color':color,'instock':instock})
    conn.commit()

    return "Product has been added", 200


app.run(port=9214,debug=True)