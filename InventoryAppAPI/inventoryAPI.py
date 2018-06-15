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

@app.route('/products/<int:id>')
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
        #add logic for POST
        pass


app.run(port=9214,debug=True)