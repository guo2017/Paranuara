import unittest

from flask import json

from server import app


class ParanuarafTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the response data
        self.assertEqual(result.data.decode('utf-8'), "This is Parranuara")

    def test_compnay_employees(self):
        # sends HTTP GET request to the application
        # on the specified path
        # if no matched employees, return error code 204

        response = self.app.get('/employees/101')
        json_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_data['error']['code'], 204)

        # assert the response data: there are employees, check the number of employees is right
        # company with id 1 has 7 employees
        response = self.app.get('/employees/1')
        json_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_data), 7)

    def test_common_friends(self):
        # sends HTTP GET request to the application
        # on the specified path
        # check if people with id 1 and 2 have common friends
        response = self.app.get('/commonfriends/1/2')
        json_data = json.loads(response.get_data(as_text=True))

        # assert the response data, the number of common friends is 1 and its name is 'Decker Mckenzie'
        self.assertEqual(len(json_data['common_friends']), 1)
        self.assertEqual(json_data['common_friends'][0]['name'], 'Decker Mckenzie')

    def test_fruits_vegetables(self):
        # sends HTTP GET request to the application
        # on the specified path
        # check if people with id 2 return right name, age, fruits and vegerables
        response = self.app.get('/fruits/2')
        json_data = json.loads(response.get_data(as_text=True))

        # assert the response data
        self.assertEqual(json_data["age"], "54")
        self.assertEqual(json_data['fruits'], ["orange", "banana", "strawberry"])
        self.assertEqual(json_data['vegetables'], ["beetroot"])
