import random
import unittest
import sys
sys.path.append('server')
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()

    def test_recommend(self):

        def createQuery():
            query = "/recommend/"
            randint1 = random.randint(-5, 200)
            randint2 = random.randint(-1, 10)

            binary = random.randint(1,2)

            if binary == 1:
                return query + str(randint1) + "/" + str(randint2) + "/"
            else:
                return query + str(randint2) + "/"
        
        for i in range(50):
            response = self.client.get(createQuery())
            bool = (response.status_code == 200) or (response.status_code == 404)
            self.assertTrue(bool)