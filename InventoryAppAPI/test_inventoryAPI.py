import unittest,json
import inventoryAPI 

class TestCase(unittest.TestCase):
    def setUp(self):
        inventoryAPI.app.config['TESTING'] = True
        self.app = inventoryAPI.app.test_client()

    def test_all_products(self):
        response = self.app.get('/products')
        

