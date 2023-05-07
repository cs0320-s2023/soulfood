import unittest
import sys
sys.path.append("server")
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()
    
    # tests searching for posts by label
    # when the label is empty
    def test_label_error(self):
        response = self.client.get('search/label/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Label should not be empty.")
    # when the label can't be found in any post
    def test_label_absent(self):
        response = self.client.get('search/label/Bad')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "No post has been assigned to this label.")
    # when the label can be found 
    def test_label_present(self):
        response = self.client.get('search/label/Chinese')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data,b'[\n]\n')


if __name__ == '__main__':
        unittest.main()