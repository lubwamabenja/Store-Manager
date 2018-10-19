import unittest
from app import app
import json


class TestProductViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_a_product(self):
        # Tests that a product is created
        post_data = ({
            'prod_id' : 0,
            'prod_name':'crisps',
            'prod_category':'snacks',
            'prod_quantity':'4 cartons',
            'unit_cost':500
        })
        response = self.client().post('/v1/products',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 302)

    def test_fetch_all_products(self):
        # Tests that the end point fetches all products
        response = self.client().get('/v1/products',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_product(self):
        # Tests that the end point successfully returns one product
        response = self.client().get('/v1/products/1',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_product_id(self):
        # Tests that the function returns invalid for wrong indices
        response = self.client().get('/v1/products/0',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)