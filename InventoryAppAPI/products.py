import sqlite3

#returns items from the database as dictioaries
def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#sets up database connection
conn = sqlite3.connect('inventory.db')
conn.row_factory = dict_factory
cur = conn.cursor()


def get_all():
    all_products = cur.execute('SELECT * FROM data').fetchall()
    return all_products


def delete_all():
    cur.execute('DELETE FROM data')
    # conn.commit()

#displays details of passed product id
def get_one_product(id):
    result = cur.execute("SELECT * FROM data WHERE productid=?",(id,)).fetchall()
    if not result:
        return 404
    else:
        return result

def update_one_product(payload,id):
    #sets up parameters
    name = payload.get('name')
    size = payload.get('size')
    color = payload.get('color')
    in_stock = payload.get('in_stock')

    #returns a 400 if no known parameters are given
    if not(name or size or color or in_stock):
        print("no known parameter given")
        return 404

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

#checks if in_stock is valid
def check_stock(instock):
    if str(instock).isdigit():
        return True
    return False