import unittest
from app.models.sales import *


class TestSaleRecords(unittest.TestCase):
    def setUp(self):
        self.record = Sales(0,'crisps','5 pkts','john',2500)
        return self.record

    def test_sale_id(self):
        # Tests that the id is equal to the given id
        self.assertNotEqual(self.record.sale_id, 1)
        self.assertNotEqual(self.record.sale_id, "str")
        self.assertEqual(self.record.sale_id, 0)

    def test_sale_id_data_type(self):
        '''tests whether sales_id is of type int'''
        self.assertNotIsInstance(self.record.sale_id, str)
        self.assertNotIsInstance(self.record.sale_id, float)
        self.assertIsInstance(self.record.sale_id, int)

    def test_prod_name(self):
        '''tests the product name given in the new record'''
        self.assertEqual(self.record.prod_name, 'crisps')
        self.assertNotEqual(self.record.prod_name, 'code')

    def test_prod_name_datatype(self):
        '''tests the datatype of the prod_name'''
        self.assertNotIsInstance(self.record.prod_name, int)
        self.assertNotIsInstance(self.record.prod_name, float)
        self.assertIsInstance(self.record.prod_name, str)


    def test_prod_quantity(self):
        # Tests that the product_quantity is equal to the given quantity
        self.assertEqual(self.record.prod_quantity, '5 pkts')
        self.assertNotEqual(self.record.prod_quantity, 'carton')
        self.assertNotEqual(self.record.prod_quantity, '1 pkt')

    def test_prod_quantity_datatype(self):
        '''Tests the datatype of the product quantity'''
        self.assertNotIsInstance(self.record.prod_quantity, int)
        self.assertNotIsInstance(self.record.prod_quantity, float)
        self.assertNotIsInstance(self.record.prod_quantity, dict)
        self.assertIsInstance(self.record.prod_quantity, str)


    def test_attendant(self):
        '''Tests the name of the attendant'''
        self.assertEqual(self.record.attendant, "john")
        self.assertNotEqual(self.record.attendant, 'lubwama')

    def test_attendant_type(self):
        '''Tessts the datatype of the attendant'''
        self.assertNotIsInstance(self.record.attendant, int)
        self.assertNotIsInstance(self.record.attendant, float)
        self.assertIsInstance(self.record.attendant, str)

    def test_price(self):
        '''Tests the price of the product'''
        self.assertEqual(self.record.price, 2500)
        self.assertNotEqual(self.record.price,1500)
       

    def test_price_datatype(self):
        ''' Tests the datatype of the price'''
        self.assertNotIsInstance(self.record.price, str)
        self.assertNotIsInstance(self.record.price, float)
        self.assertIsInstance(self.record.price, int)

