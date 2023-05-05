import unittest
import sys
sys.path.append('server')
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()

    # tests for recommendation
    # when both uid and num_recommend are not provided
    def test_empty(self):
        response = self.client.get('/recommend/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.error, 'Recommnedation cannot be given to unspecified user')

    # when num_recommend is not provided
    # when uid < 0
    def test_default_uid_negative(self):
        response = self.client.get('/recommend/-2/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.error, "User id should be nonnegative")
    # when uid is nonexistant
    def test_default_uid_invalid(self):
        response = self.client.get('/recommend/100000000/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.error, "This user does not exist")
    # when uid is valid
    def test_default(self):
        response = self.client.get('/recommend/10/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, )
