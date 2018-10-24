import unittest
from app import app


class FlaskTestCase(unittest.TestCase):
	"""Enasure that flask was set up correctly"""
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('v1/login',content_type='html/text')
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(response.status_code,405)

	"""Ensure that the login page logs in correctly"""
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('v1/login',content_type='html/text')
		self.assertTrue(b'Please login' in response.data)
		self.assertFalse(b'Please logout' in response.data)

	''' Ensure login page loads correctly given correct credentials '''
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'v1/login',
			data = dict(username="admin", password="admin"),
			follow_redirects=True)
		self.assertIn(b'You were logged in!', response.data)
		self.assertNotIn(b'Invalid Credentials. Please try again.', response.data)


	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'v1/login',
			data = dict(username="wrong", password="wrong"),
			follow_redirects=True)
		self.assertIn(b'Invalid Credentials. Please try again.', response.data)
		self.assertNotIn(b'Invalid Credentials. Please try later.', response.data)
     

	
	'''Ensure that main page  does not require login '''
	def test_main_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/v1',follow_redirects = True)
		self.assertFalse(b'You need to login first.' in response.data)

	'''Ensure that main page requires login '''
	def test_logout_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/v1/logout',follow_redirects = True)
		self.assertTrue(b'You need to login first.' in response.data)
		self.assertFalse(b'See your self.' in response.data)


