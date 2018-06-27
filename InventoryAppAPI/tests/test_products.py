from InventoryAppAPI import products
from unittest import TestCase
from nose.tools import assert_true,assert_is_not_none, assert_false
import requests, sqlite3
from unittest.mock import patch
import unittest, json

#declars global database stack in memory
global DB, cursor
DB = sqlite3.connect(':memory:')
cursor = DB.cursor()

class ProductsTests(TestCase):
    
    #creates a table data in memory and importes the data from inventory.db to it 
    def setUp(self):
        super().setUp()
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
        DB.close()
        super().tearDown()
    
    """############## DATABASE TESTS ##############"""
    def test_GET_all_is_empty(self):
        DB.row_factory = products.dict_factory
        all_products = cursor.execute('SELECT * FROM data').fetchall()
        self.assertFalse(all_products == None)
    def test_GET_all_is_not_empty(self):
        DB.row_factory = products.dict_factory
        all_products = cursor.execute('SELECT * FROM data').fetchall()
        assert_is_not_none(all_products)
    def test_GET_one_valid_item(self):
        item = products.get_one_product(DB,cursor,1234567)
        assert item == [("1234567","oversized coat","M","red",23)]
    def test_GET_invalid_items(self):
        item = products.get_one_product(DB,cursor,9999999)
        assert item == 404
        item = products.get_one_product(DB,cursor,9234)
        assert item == 404 
        item = products.get_one_product(DB,cursor,'very bad input')
        assert item == 404
        item = products.get_one_product(DB,cursor,'')
        assert item == 404

    """############## WEB SERVICE TESTS ##############"""
    def test_GET_all_returns_json_file(self):
        #checks if GET all_products returns a json file
        url = 'http://127.0.0.1:9214/products/'
        response = requests.get(url)
        assert response.headers['content-type'] == 'application/json'
        assert response.status_code == 200

    def test_GET_all_does_not_return_an_empty_json(self):
        url = 'http://127.0.0.1:9214/products/'
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data != None
    
    def test_DELETE_valid_item(self):
        #checks that deleting a valid item returns 200 of type json
        url = 'http://127.0.0.1:9214/products/1234567'
        response = requests.delete(url)
        assert response.status_code == 200

    def test_DELETE_invalid_item(self):
        #checks that deleting an invalid item returns 404 of type json
        url = 'http://127.0.0.1:9214/products/9999888'
        response = requests.delete(url)
        assert response.status_code == 404

    def test_DELETE_gibirish(self):
        #checks that adding anything after the requested url returns a json 404
        url = 'http://127.0.0.1:9214/products/laskdjflasdjflsd'
        response = requests.delete(url)
        assert response.status_code == 400

    def test_PUT_product_of_valid_json_payload(self):
        #checks that the json payload is valid (test multiple payloads) (check for status also)

        url = 'http://127.0.0.1:9214/products/add'
        payload ={"name":"testing jacket","in_stock":"83","product_id":"6464645","size":"L","color":"grey"}
        response = requests.put(url,data=payload)
        assert response.status_code == 200

        payload ={"in_stock":66,"product_id":"1111111"}
        response = requests.put(url,data=payload)
        assert response.status_code == 200

    def test_PUT_product_of_invalid_json_payload(self):
        #checks that the json payload is invalid and handled properly (i.e. check for status and type)
        pass

    def test_PUT_repeated_ID(self):
        #check if the server returns a conflic status code when adding a repeated item
        pass

    # def test_

    # #mocks a PUT request to test adding a new item
    # def test_PUT_add_new_product(self):
    #     url = 'http://127.0.0.1:9214/products/add'
    #     payload = {
    #         "name":"some item",
    #         "color":"red",
    #         "size":"M",
    #         "in_stock":23,

    #         "product_id":"8273843"
    #     }
    #     headers = {"x-api-key":"test_api_dp"}
    #     response = requests.put(url,json=payload,headers=headers)
    #     assert response.status_code == 200 or 409 #RETURNS 200 WHEN ADDING A NEW ITEM OR 409 IF THE ITEM EXISTS.




    # test insert a product
    # 1. assert there is no product
    # 2. import products
    # 3. assert get all products returns the imported product




    #This method mocks a GET request but needs the server to be running
    # def test_request_response(self):
    #     #tests getting all items
    #     response = requests.get('http://127.0.0.1:9214/products/')
    #     assert_true(response.ok)
    #     #tests getting one product
    #     response = requests.get('http://127.0.0.1:9214/products/8374345')
    #     assert_true(response.ok)
    #     #tests searching capabilities
    #     response = requests.get('http://127.0.0.1:9214/products/search?name=shirt')
    #     assert_true(response.ok)