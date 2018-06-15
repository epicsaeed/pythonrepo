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

app.run(port=9214,debug=True)