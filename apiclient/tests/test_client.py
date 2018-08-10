from apiclient import client
import unittest

class ClientTests(unittest.TestCase):

    def setUp(self):
        super().setUp()
        #initiate variables:
        global validPID, inValidPIDs
        validPID = 1234567
        inValidPIDs = ["asdkfaksjhf",6666666,"ssd6452"]

    def tearDown(self):
        super().tearDown()

    def test_get_all(self):
        assert client.GETAll() is not None

    def get_valid_item(self):
        assert client.GETOne(validPID) != False

    