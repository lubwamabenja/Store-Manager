import unittest
from app import app
from flask import json


class TestSaleViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_a_sale(self):
        # Tests that a sale record is created
        post_data = ({
            'sale_id': 1,
            'prod_name': 'ethernet',
            'prod_quantity':'1 m',
            'price':10000,
            'attendant':'peter'
        })
        response = self.client().post('/v1/sales',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 302)

    def test_fetch_all_sales(self):
        # Tests that the end point fetches all sale records
        response = self.client().get('/v1/sales',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 302)

    def test_fetch_a_single_record(self):
        # Tests that the end point successfully returns a single sale record
        response = self.client().get('/v1/sales/1',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 302)

    def test_fetch_one_sale_id(self):
        # Tests that the function returns invalid for wrong indices
        response = self.client().get('/v1/sales/0',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 302)
