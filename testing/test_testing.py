import unittest
from InventoryAppAPI.inventoryAPI import app

class InventoryTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass 


    def test_all_products_status_code(self):
        result = self.app.get('/products/')
        self.assertEqual(result.status_code,200)

    def test_all_products_data(self):
        result = self.app.get('/products/')
        self.assertEqual(result.data, 'json/application')




# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
