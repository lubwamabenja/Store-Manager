import unittest
from app import app
import json
from app.models.users import *


class TestProductViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.user_record = Users(1,'lubwama','lubwama1','true')
        return self.user_record

    def test_user_creation(self):
	# Tests that the user already exists
        post_data = ({
            'username':'lubwama',
            'password':"123455"
        })


        response = self.client.post('/v2/users',
                                     content_type='application/json',
                                     data = json.dumps(post_data))
        #self.assertTrue(post_data['message']=='user already exists')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,500)
        self.assertTrue(response.content_type == 'application/json')


    def test_user_login(self):
    	with self.client:
    		resp_login = self.client.post(
    			'/auth/login',
    			data=json.dumps(dict(
    				username = 'lubwama',
    				password = 'lubwama1')),
    			content_type = 'application/json')

    		data_login = json.loads(resp_login.data.decode())
    	self.assertTrue(data_login['message'] == 'successfully logged in')
    	self.assertTrue(resp_login.content_type =='application/json')
    	self.assertTrue(resp_login.status_code == 200)
    	self.assertFalse(resp_login.status_code ==500)
    	self.assertTrue(data_login['token'])


    def test_get_user_without_token(self):
    	with self.client:
    		resp_login = self.client.get(
    			'/v2/users',
    	
    			content_type = 'application/json')

    	self.assertTrue(resp_login.content_type =='application/json')
    	self.assertEqual(resp_login.status_code,401)
    	self.assertNotEqual(resp_login.status_code,500)


    def test_get_user_with_token(self):
    	with self.client:

    		resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
    		response = self.client.get(
    			'/v2/users',
    			headers=dict(
                            Authorization='Bearer ' + 
                            resp_login.get_json()["token"]),
    						content_type = 'application/json')

    	self.assertTrue(response.content_type =='application/json')
    	self.assertEqual(response.status_code,200)
    	self.assertNotEqual(response.status_code,500)


    def promote_user(self):
    	with self.client:

    		resp_login = self.client.post('/auth/login',
                                json=dict(
                                username='lubwama',
                                password='lubwama1'))
    		response = self.client.put(
    			'/v2/users<user_id>',
    			headers=dict(
                            Authorization='Bearer ' + 
                            resp_login.get_json()["token"]),
    						content_type = 'application/json')
        
    	self.assertTrue(response.content_type =='application/json')
    	self.assertEqual(response.status_code,200)
    	self.assertNotEqual(response.status_code,500)


    def test_user_id(self):
        # Tests that the id is equal to the given id
        self.assertEqual(self.user_record.user_id,1)
        self.assertNotEqual(self.user_record.user_id, 9)
        self.assertNotEqual(self.user_record.user_id, "str")
        self.assertNotEqual(self.user_record.user_id, 0)

    def test_user_id_data_type(self):
        self.assertNotIsInstance(self.user_record.user_id, str)
        self.assertNotIsInstance(self.user_record.user_id, float)
        self.assertIsInstance(self.user_record.user_id, int)

        
    def test_username(self):
        '''tests the product name given in the new user_record'''
        self.assertEqual(self.user_record.username, 'lubwama')
        self.assertNotEqual(self.user_record.username, 'code')

    def test_username_datatype(self):
        '''tests the datatype of the username'''
        self.assertNotIsInstance(self.user_record.username, int)
        self.assertNotIsInstance(self.user_record.username, float)
        self.assertIsInstance(self.user_record.username, str)

    def test_password(self):
        '''Tests the name of the prod_category'''
        self.assertEqual(self.user_record.password, 'lubwama1')
        self.assertNotEqual(self.user_record.password, 'lubwama')

    def test_password_datatype(self):
        '''Tessts the datatype of the prod_category'''
        self.assertNotIsInstance(self.user_record.password, int)
        self.assertNotIsInstance(self.user_record.password, float)
        self.assertIsInstance(self.user_record.password, str)





   


