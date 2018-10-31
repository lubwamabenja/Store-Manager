import unittest
from app import app
import json


class TestProductViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_a_product(self):
        # Tests that a product is created
        post_data = ({
            'prod_name':'phones',
            'prod_quantity':3,
            'unit_cost':1700,
            'category_name':'Electronics'
        })
        response = self.client.post('/v2/products',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)
