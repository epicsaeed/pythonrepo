import sqlite3, random

global conn,cur
conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_all():
    #sets up database connection
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_products = cur.execute('SELECT * FROM data').fetchall()
    return all_products

def delete_all():
    #sets up database connection
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('DELETE FROM data')
    # conn.commit()

#displays details of passed product id
def get_one_product(conn,cur,id):
    #sets up database connection

    result = cur.execute("SELECT * FROM data WHERE productid=?",(id,)).fetchall()
    if not result:
        return 404
    else:
        return result

def update_one_product(conn,cur,payload,id,):

    #sets up parameters
    name = payload.get('name')
    size = payload.get('size')
    color = payload.get('color')
    in_stock = payload.get('in_stock')

    #checks if the passed product id exists
    exists = get_one_product(conn,cur,id)
    if exists == 404:
        return 404

    #returns a 400 if no known parameters are given
    if not(name or size or color or in_stock):
        return 400

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
        if check_stock(in_stock):
            query = "UPDATE data SET instock =? WHERE productid=?"
            cur.execute(query,(in_stock,id))
            conn.commit()
        else:
           return 404

    return 200

def search_in_db(conn,cur,query_parameters):
    conn.row_factory = dict_factory

    #checks for inserted parameters 
    id = query_parameters.get('productid')
    print(query_parameters.get('productid'))
    name = query_parameters.get('name')
    size = query_parameters.get('size')
    color = query_parameters.get('color')
    
    query = "SELECT * FROM data WHERE"
    to_filter = []

    if not (id or name or size or color):
        return 404

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

    query = query[:-4]

    results = cur.execute(query,to_filter).fetchall()
    return results

#checks if in_stock is valid
def check_stock(instock):
    if str(instock).isdigit():
        return True
    return False

def add_new_product(conn,cur,payload):

    details = {"name":"","product_id":"","size":"","color":"","in_stock":""}

    if "product_id" in payload:
        pid = str(payload['product_id'])
        details["product_id"]=pid
        if not pid.isdigit() or len(pid) != 7:
            return 404
    else:
        return 404

    if "in_stock" in payload:
        instock = str(payload['in_stock'])
        details["in_stock"]=instock
        if not instock.isdigit() or not instock:
            return 404
    else:
        return 404

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
            return 409

    cur.execute("INSERT INTO data VALUES(:productid,:name,:size,:color,:instock)",{'productid':pid,'name':name,'size':size,'color':color,'instock':instock})
    conn.commit()

    return details

def delete_one_product(id):
    #checks if the pid exists in DB and returns 404 if not
    cur.execute("SELECT * FROM data WHERE productid = ?",(id,))
    data = cur.fetchall()
    if len(data) == 0:
        return 404
    else:
        cur.execute("DELETE FROM data WHERE productid =?",(id,))
        conn.commit()
        return 200

def random_pid():
    return random.randint(0000000,9999999)