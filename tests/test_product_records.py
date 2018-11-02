import unittest
from app.models.products import *


class TestProductprod_records(unittest.TestCase):
    def setUp(self):
        self.prod_record = Products(4,'crisps','snacks','4cartons',500)
        return self.prod_record

    def test_prod_id(self):
        # Tests that the id is equal to the given id
        self.assertNotEqual(self.prod_record.prod_id, 1)
        self.assertNotEqual(self.prod_record.prod_id, "str")
        self.assertEqual(self.prod_record.prod_id, 4)

    def test_prod_id_data_type(self):
        self.assertNotIsInstance(self.prod_record.prod_id, str)
        self.assertNotIsInstance(self.prod_record.prod_id, float)
        self.assertIsInstance(self.prod_record.prod_id, int)

        
    def test_prod_name(self):
        '''tests the product name given in the new prod_record'''
        self.assertEqual(self.prod_record.prod_name, 'crisps')
        self.assertNotEqual(self.prod_record.prod_name, 'code')

    def test_prod_name_datatype(self):
        '''tests the datatype of the prod_name'''
        self.assertNotIsInstance(self.prod_record.prod_name, int)
        self.assertNotIsInstance(self.prod_record.prod_name, float)
        self.assertIsInstance(self.prod_record.prod_name, str)

    def test_prod_category(self):
        '''Tests the name of the prod_category'''
        self.assertEqual(self.prod_record.prod_category, 'snacks')
        self.assertNotEqual(self.prod_record.prod_category, 'lubwama')

    def test_prod_category_type(self):
        '''Tessts the datatype of the prod_category'''
        self.assertNotIsInstance(self.prod_record.prod_category, int)
        self.assertNotIsInstance(self.prod_record.prod_category, float)
        self.assertIsInstance(self.prod_record.prod_category, str)



    def test_prod_quantity(self):
        # Tests that the prod_quantity is equal to the given quantity
        self.assertEqual(self.prod_record.prod_quantity, '4cartons')
        self.assertNotEqual(self.prod_record.prod_quantity, 'carton')
        self.assertNotEqual(self.prod_record.prod_quantity, '1 pkt')

    def test_prod_quantity_datatype(self):
        '''Tests the datatype of the product quantity'''
        self.assertNotIsInstance(self.prod_record.prod_quantity, int)
        self.assertNotIsInstance(self.prod_record.prod_quantity, float)
        self.assertNotIsInstance(self.prod_record.prod_quantity, dict)
        self.assertIsInstance(self.prod_record.prod_quantity, str)


    
    def test_unit_cost(self):
        '''Tests the unit_cost of the product'''
        self.assertEqual(self.prod_record.unit_cost, 500)
        self.assertNotEqual(self.prod_record.unit_cost,1500)
       

    def test_unit_cost_datatype(self):
        ''' Tests the datatype of the unit_cost'''
        self.assertNotIsInstance(self.prod_record.unit_cost, str)
        self.assertNotIsInstance(self.prod_record.unit_cost, float)
        self.assertIsInstance(self.prod_record.unit_cost, int)

