from InventoryAppAPI import products
from unittest import TestCase
from nose.tools import assert_true,assert_is_not_none
import requests, sqlite3
from unittest.mock import patch
import unittest

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

    def test_GET_all_is_not_empty(self):
        DB.row_factory = products.dict_factory
        all_products = cursor.execute('SELECT * FROM data').fetchall()
        assert_is_not_none(all_products)

    def test_GET_all_is_empty(self):
        DB.row_factory = products.dict_factory
        all_products = cursor.execute('SELECT * FROM data').fetchall()
        assert all_products != None

    def test_GET_one_valid_item(self):
        #ensures the request returns the cirrect details 
        item = products.get_one_product(DB,cursor,1234567)
        assert item == [("1234567","some item","M","red",23)]

    def test_GET_invalid_items(self):
        item = products.get_one_product(DB,cursor,9999999)
        assert item == 404
        item = products.get_one_product(DB,cursor,9234)
        assert item == 404 
        item = products.get_one_product(DB,cursor,'very bad input')
        assert item == 404
        item = products.get_one_product(DB,cursor,'')
        assert item == 404

    #checks if the search function works correctly
    # def test_GET_search_for_item(self):







        # URL = 'http://127.0.0.1:9214/products/search'
        # query = "jacket"
        # PARAMS = {'name':query}
        # response = requests.get(url = URL, params = PARAMS)
        # data = response.json()
        # assert response.status_code == 200
        # print(data)

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