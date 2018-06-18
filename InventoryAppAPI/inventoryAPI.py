from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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

        #conn.close()

        return "Product has been updated", 200
    #deletes item of passed product id
    elif request.method == 'DELETE':

        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        exist = []
        #checks if the pid exists in DB and returns a conflict error status code
        cur.execute("SELECT * FROM data WHERE productid LIKE ?",(id,))
        for row in cur.fetchall():
            exist.append(row)
            if not exist:
                return jsonify(), 404
            else:
                cur.execute("DELETE FROM data WHERE  productid =?",(id,))
                conn.commit()
                return jsonify(),200
    else:
        return jsonify(),404


@app.route('/products/add',methods=['PUT'])
def api_add():
    payload = request.get_json()

    if "product_id" in payload:
        pid = str(payload['product_id'])
        if not pid.isdigit() or len(pid) != 7:
            return jsonify(),404
    else:
        return jsonify(),404

    if "in_stock" in payload:
        instock = str(payload['in_stock'])
        if not instock.isdigit() or not instock:
            return jsonify(),404
    else:
        return jsonify(),404

    if "name" in payload:
        name = payload['name']
    else:
        name = "N/A"
    
    if "size" in payload:
        size = payload['size']
    else:
        size = "N/A"

    if "color" in payload:
        color = payload['color']
    else:
        color = "N/A"

    # #checks if pid or availability is not based in json paylad
    # if ('product_id' and 'in_stock') not in payload:
    #     return jsonify(),404
    # #checks if product id is invalid
    # elif not payload['product_id'] or len(payload['product_id']) != 7 or not payload['product_id'].isdigit():
    #     return jsonify(),404
    # #checks if availability is invalid
    # elif not payload['in_stock'] or not payload['in_stock'].isdigit():
    #     return jsonify(),404
    # else:
    #     pid = payload['product_id']
    #     instock = payload['in_stock']
    #     name = payload['name']
    #     size = payload['size']
    #     color = payload['color']

    # if not pid:

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

    return  jsonify(),200


app.run(port=9214,debug=True)