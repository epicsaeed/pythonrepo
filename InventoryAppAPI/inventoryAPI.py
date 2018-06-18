from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#routes to the home page of the server
# @app.route('/',methods=['GET'])
# def main():
#     return "<h1>Inventory App</h1><p>This is a web server for inventory.</p>"

#displays all products in the database
@app.route('/products/',methods=['GET'])
def api_all():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_products = cur.execute('SELECT * FROM data').fetchall()
    return jsonify(all_products)

#displays details of specific id, deletes a product, updates a product
@app.route('/products/<int:id>',methods=['POST','GET','DELETE'])
def api_product(id):
    #displays details of passed product id
    if request.method == 'GET':

        query = "SELECT * FROM data WHERE productid=%s;"%id

        conn = sqlite3.connect('inventory.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        result = cur.execute(query).fetchall()
        
        if not result:
            return jsonify(),404
        else:
            return jsonify(result)

    #updates details of passed product id
    elif request.method == 'POST':
        
        payload = request.get_json()

        #initiates database
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()

        if "name" in payload:
            name = payload['name'] 
            query = "UPDATE data SET name =? WHERE productid=?"
            cur.execute(query,(name,id))
            conn.commit()

        if "size" in payload:
            size = payload['size']
            query = "UPDATE data SET size =? WHERE productid=?"
            cur.execute(query,(size,id))
            conn.commit()

        if "color" in payload:
            color = payload['color']
            query = "UPDATE data SET color =? WHERE productid=?"
            cur.execute(query,(color,id))
            conn.commit()

        if "in_stock" in payload:
            instock = payload['in_stock']
            query = "UPDATE data SET instock =? WHERE productid=?"
            cur.execute(query,(instock,id))
            conn.commit()
        
        if ('name' and 'size' and 'color' and 'in_stock') not in payload:
            return jsonify(),404

        conn.close()

        return "Product has been updated", 200
    #deletes item of passed product id
    elif request.method == 'DELETE':

        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM data WHERE  productid =?",(id,))
        conn.commit()
        conn.close()

        return jsonify(),200

    else:
        return 405


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

    return  jsonify(),200


app.run(port=9214,debug=True)