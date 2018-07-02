from InventoryAppAPI import products
from unittest import TestCase
from nose.tools import assert_true,assert_is_not_none, assert_false
import requests, sqlite3
from unittest.mock import patch
import unittest, json, random

class ProductsTests(TestCase):

    #creates a table data in memory and importes the data from inventory.db to it 
    def setUp(self):
        super().setUp()
        #declars global database stack in memory
        global DB, cursor
        DB = sqlite3.connect(':memory:')
        cursor = DB.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS data(productid TEXT, name TEXT,size TEXT, color TEXT, instock INTEGER)''')
        DB.commit()
        productsdict = products.get_all()

        pid = []
        n = []
        s = []
        c = []
        stock = []
        count = 0
        for items in productsdict:
            pid.append(items['productid'])
            n.append(items['name'])
            s.append(items['size'])
            c.append(items['color'])
            stock.append(items['instock'])
        L = len(pid)
        while L > count:
            cursor.execute('''INSERT INTO data (productid,name,size,color,instock) VALUES(?,?,?,?,?)''',(pid[count],n[count],s[count],c[count],stock[count]))
            count+=1
        pid.clear()
        n.clear()
        s.clear()
        c.clear()
        stock.clear()

    #wibes the database stack in memory
    def tearDown(self):
        cursor.execute("DELETE FROM data")
        DB.commit()
        super().tearDown
    
    """############## MEMORY DATABASE TESTS ##############"""
    
    def test_GET_all_is_empty(self):
        DB.row_factory = products.dict_factory
        all_products = cursor.execute('SELECT * FROM data').fetchall()
        self.assertFalse(all_products == None)
    
    def test_GET_all_is_not_empty(self):
        DB.row_factory = products.dict_factory
        all_products = cursor.execute('SELECT * FROM data').fetchall()
        assert_is_not_none(all_products)
    
    def test_GET_one_valid_item(self):
        item = products.get_one_product(DB,cursor,9465312)
        item = item[0]
        assert item['productid'] == '9465312'
    
    def test_GET_invalid_items(self):
        item = products.get_one_product(DB,cursor,9999999)
        assert item == 404
        item = products.get_one_product(DB,cursor,9234)
        assert item == 404 
        item = products.get_one_product(DB,cursor,'very bad input')
        assert item == 404
        item = products.get_one_product(DB,cursor,'')
        assert item == 404

    def test_POST_valid_pid_db(self):
        payload = {"name":"HAS BEEN UPDATED","in_stock":99}
        id = 1234567
        update_status = products.update_one_product(DB,cursor,payload,id)
        assert update_status == 200

    def test_POST_invalid_pid_db(self):
        payload = {"name":"changing the name","in_stock":99}
        id = random.randint(0000000,9999999)
        update_status = products.update_one_product(DB,cursor,payload,id)
        assert update_status == 404
        
    def test_POST_invalid_payload_db(self):
        payload = {}
        id = 1234567
        update_status = products.update_one_product(DB,cursor,payload,id)
        assert update_status == 400

        payload = {"product_id":"3452875"}
        update_status = products.update_one_product(DB,cursor,payload,id)
        assert update_status == 400

    def test_PUT_valid_json_payload(self):
        pid = products.random_pid()
        payload = {"product_id":pid,"name":"testing","size":"EU40","color":"orange","in_stock":545}
        add_status = products.add_new_product(DB,cursor,payload)
        assert add_status['product_id'] == str(pid)

    def test_PUT_invalid_json_payload(self):
        payload = {}
        add_status = products.add_new_product(DB,cursor,payload)
        assert add_status == 404

        payload = {"nothing":"foo"}
        add_status = products.add_new_product(DB,cursor,payload)
        assert add_status == 404

        payload = {"name":"testing","size":"EU40","color":"orange"}
        add_status = products.add_new_product(DB,cursor,payload)
        assert add_status == 404

    def test_PUT_repeated_pid(self):
        payload = {"product_id":"1234567","in_stock":888}
        add_status = products.add_new_product(DB,cursor,payload)
        assert add_status == 409

    def test_DELETE_valid_pid_db(self):
        delete_status = products.delete_one_product(1234567)
        assert delete_status == 200

    def test_DELETE_invalid_pid_db(self):
        delete_status = products.delete_one_product(9999999)
        assert delete_status == 404

    
    """############## WEB SERVICE TESTS ##############"""

    def test_GET_all_returns_json_file(self):
        #checks if GET all_products returns a json file
        url = 'http://127.0.0.1:9214/products/'
        response = requests.get(url)
        assert response.headers['content-type'] == 'application/json'
        assert response.status_code == 200

    def test_GET_all_returns_dict(self):
        url = 'http://127.0.0.1:9214/products/'
        response = requests.get(url)
        entry = response.json()[0]
        assert ('name' and 'color' and 'size' and 'productid' and 'instock') in entry

    def test_GET_all_does_not_return_non_dict(self):
        url = 'http://127.0.0.1:9214/products/'
        response = requests.get(url)
        entry = response.json()[0]
        assert_false('name' and 'color' and 'size' and 'productid' and 'instock' not in entry)

    def test_GET_all_does_not_return_an_empty_json(self):
        url = 'http://127.0.0.1:9214/products/'
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data != None
    
    def test_GET_product_of_valid_pid(self):
        url = 'http://127.0.0.1:9214/products/9554144'
        response = requests.get(url)
        assert response.status_code == 200
        assert response.headers['content-type'] == 'application/json'
        assert response.headers['content-length'] == '131'

    def test_GET_product_of_invalid_pid(self):
        url = 'http://127.0.0.1:9214/products/1111111'
        response = requests.get(url)
        assert response.status_code == 404

    def test_GET_product_returns_dict(self):
        url = 'http://127.0.0.1:9214/products/9283783'
        response = requests.get(url)
        json = response.json()[0]
        assert ('name' and 'color' and 'size' and 'productid' and 'instock') in json
        
    def test_DELETE_valid_pid(self):
        #checks that deleting a valid item returns 200 of type json
        url = 'http://127.0.0.1:9214/products/1234567'
        response = requests.delete(url)
        assert response.status_code == 200

    def test_DELETE_invalid_pid(self):
        #checks that deleting an invalid item returns 404 of type json
        url = 'http://127.0.0.1:9214/products/3213215'
        response = requests.delete(url)
        assert response.status_code == 404

    def test_DELETE_anything(self):
        #checks that adding anything after the requested url returns a json 404
        url = 'http://127.0.0.1:9214/products/laskdjflasdjflsd'
        response = requests.delete(url)
        assert response.status_code == 400

    def test_PUT_product_of_valid_json_payload(self):
        #checks that the json payload is valid (test multiple payloads) (check for status also)
        url = 'http://127.0.0.1:9214/products/add'
        pid = products.random_pid()
        payload ={"name":"testing","in_stock":42,"product_id":pid,"size":"L","color":"grey"}
        response = requests.put(url,json=payload)
        assert response.status_code == 200
        products.delete_one_product(pid)

        pid = products.random_pid()
        payload ={"in_stock":66,"product_id":pid}
        response = requests.put(url,json=payload)
        assert response.status_code == 200
        products.delete_one_product(pid)

    def test_PUT_product_of_invalid_json_payload(self):
        #checks that the json payload is invalid and handled properly (i.e. check for status and type)
        url = 'http://127.0.0.1:9214/products/add'
        payload ={"in_stock":66,"product_id":"000000000000"}
        response = requests.put(url,json=payload)
        assert response.status_code == 404
        
        payload["product_id"] = "something not valid"
        response = requests.put(url,json=payload)
        assert response.status_code == 404

        payload ={}
        response = requests.put(url,json=payload)
        assert response.status_code == 400 

    def test_PUT_repeated_ID(self):
        #check if the server returns a conflic status code when adding a repeated item
        url = 'http://127.0.0.1:9214/products/add'
        payload = {"product_id":"8374345","in_stock":99}
        response = requests.put(url,json=payload)
        assert response.status_code == 409

    def test_PUT_returns_the_added_item(self):
        url = 'http://127.0.0.1:9214/products/add'
        pid = products.random_pid()
        payload ={"name":"testing PUT","in_stock":42,"product_id":pid}
        requests.put(url,json=payload)

        pid = str(pid)
        url = 'http://127.0.0.1:9214/products/' + pid
        response = requests.get(url)
        json = response.json()
        json = json[0]
        checkPoint = json['productid']
        assert pid in checkPoint
        products.delete_one_product(pid)

    def test_POST_valid_pid(self):
        #used to test that updating a valid product id
        url =  'http://127.0.0.1:9214/products/1234567'
        payload = {"name":"something updated"}
        response = requests.post(url,json=payload)
        assert response.status_code == 200

    def test_POST_invalid_pid(self):
        #used to test that updating an invalid product id returns 404
        url =  'http://127.0.0.1:9214/products/9999333'
        payload = {"in_stock":12}
        response = requests.post(url,json=payload)
        assert response.status_code == 404

    def test_POST_valid_payload(self):
        #test updating a product with a valid json payload
        url =  'http://127.0.0.1:9214/products/1234567'
        payload = {"name":"something"}
        response = requests.post(url,json=payload)
        assert response.status_code == 200

    def test_POST_invalid_payload(self):
        #test updating a product with an invalid json payload
        url =  'http://127.0.0.1:9214/products/1234567'
        payload = {}
        response = requests.post(url,json=payload)
        assert response.status_code == 400

        payload["instock"] = 33
        response = requests.post(url,json=payload)
        assert response.status_code == 400

    def test_GET_search_invalid_query(self):
        url = 'http://127.0.0.1:9214/products/search'
        query = {}
        response = requests.get(url,params=query)
        assert response.status_code == 404 and response.headers['Content-Type'] == 'application/json'

        query = {"invalid parameter":"bad payload"}
        response = requests.get(url,params=query)
        assert response.status_code == 404 and response.headers['Content-Type'] == 'application/json'

        query = {"sdfsd":234234}
        response = requests.get(url,params=query)
        assert response.status_code == 404 and response.headers['Content-Type'] == 'application/json'

    def test_GET_search_valid_query(self):
        url = 'http://127.0.0.1:9214/products/search'

        query = {"name":"jacket"}
        response = requests.get(url,params=query)
        assert response.status_code == 200 and response.headers['Content-Type'] == 'application/json'

        query = {"size":"large"}
        response = requests.get(url,params=query)
        assert response.status_code == 200 and response.headers['Content-Type'] == 'application/json'

    def test_GET_search_returns_dict(self):
        url = 'http://127.0.0.1:9214/products/search'
        query = {"name":"jacket"}
        response = requests.get(url,params=query)
        json = response.json()
        json = json[0]
        assert 'productid' and 'instock' in json

