import unittest
from app import app
import json
from app.models.database import *


class TestProductViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_a_product(self):
        # Tests that a product is created
        post_data = ({
            'prod_name':'',
            'prod_quantity':3,
            'unit_cost':1700,
            'category_name':'Electronics'
        })
        resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
                                    
                                    
        response = self.client.post('/v2/products',
                                    headers=dict(
                                    Authorization='Bearer ' + 
                                    resp_login.get_json()["token"]),
                                    content_type='application/json',
                                    data = json.dumps(post_data))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)


    def test_fetch_all_products(self):
        # Tests that the end point fetches all products
        with self.client:

            resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
            response = self.client.get(
                '/v2/products',
                headers=dict(
                            Authorization='Bearer ' + 
                            resp_login.get_json()["token"]),
                            content_type = 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)

    def test_fetch_product_by_id(self):
        # Tests that the end point fetches a product by id
        with self.client:
            resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
            response = self.client.get(
                '/v2/products/1',
                headers=dict(
                            Authorization='Bearer ' + 
                            resp_login.get_json()["token"]),
                            content_type = 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)


    def test_modify_roduct(self):
        # Tests that a product is created
        new_data = ({
            'prod_name':'',
            'prod_quantity':3,
            'unit_cost':1700,
            'category_name':'Electronics'
        })
        resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
                                    
                                    
        response = self.client.put('/v2/products/1',
                                    headers=dict(
                                    Authorization='Bearer ' + 
                                    resp_login.get_json()["token"]),
                                    content_type='application/json',
                                    data = json.dumps(new_data))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)
        self.assertTrue(response.content_type == 'application/json')


    def delete_product(self):
        # Tests that the end point fetches a product by id
        with self.client:
            resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
            response = self.client.delete(
                '/v2/products/1',
                headers=dict(
                            Authorization='Bearer ' + 
                            resp_login.get_json()["token"]),
                            content_type = 'application/json')

            data_login = json.loads(resp_login.data.decode())
        self.assertTrue(data_login['message'] == 'successfully logged in')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)
        self.assertTrue(response.content_type == 'application/json')


        








 