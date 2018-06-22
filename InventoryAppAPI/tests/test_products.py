from InventoryAppAPI import products
from unittest import TestCase

class ProdctsTests(TestCase):
    def setUp(self):
        super().setUp()
        products.delete_all()
        # /'#' insert one product

    def tearDown(self):
        products.delete_all()
        super().tearDown()

    def test_get_all(self):
        #ensures we import a list
        assert products.get_all() != []
        #ensures we imported the correct columns
        assert 'color' and 'instock' and 'size' and 'productid' and 'name' in products.get_all()[0]

    def test_get_one_item(self):
        #checks if functions returns correct type
        item = products.get_one_product(8374345)
        self.assertIsInstance(item, list)

        #ensures non existant products return a 404 status code
        item = products.get_one_product(1234567)
        assert item == 404

        #enures incorrect statements return a 404 status code
        item = products.get_one_product('aoduasduihfu')
        assert item == 404


    # test insert a product
    # 1. assert there is no product
    # 2. import products
    # 3. assert get all products returns the imported product