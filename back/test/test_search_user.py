import unittest
import sys
sys.path.append("server")
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()

    # tests searching for user by uid
    # when the user id is not provided
    def test_user_empty(self):
        response = self.client.get('/search/user/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "User id should not be empty")
    # when the user id is less than 0
    def test_user_invalid(self):
        response = self.client.get('/search/user/-2')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'{\n"error":"User id should be nonnegative"\n}\n')
    # when the user with that id doesn't exist
    def test_user_absent(self):
        response = self.client.get('/search/user/201')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "This user does not exist.")
    # when the user with that id exists
    def test_user_present(self):
        response = self.client.get('search/user/121')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["uid"],121)
        self.assertEqual(response.json["id"],"Sample_id")
        self.assertEqual(response.json["bio"], "Sample_bio")
        self.assertEqual(response.json["following"], [1, 2, 16, 33, 38, 43, 44, 48, 49, 50, 65, 71, 72, 76, 79, 83, 84, 93, 108, 111, 112, 118, 125, 126, 128, 154, 159, 163, 164, 165, 179, 187, 190])
        self.assertEqual(response.json["followed_by"], [92, 148, 160, 186, 150, 178, 74, 75, 192, 118, 43, 165, 149, 137, 147, 103, 41, 167, 26, 98, 164, 68, 128, 46, 157, 19, 105, 36])
        self.assertEqual(response.json["liked"], [3, 6, 11, 54, 67, 73, 87, 89, 92, 97, 101, 116, 119, 129, 130, 142, 144, 154, 156, 158, 163, 166, 167, 173, 174, 178, 179, 193, 195, 200, 207, 218, 219, 224, 234, 236, 240, 248, 252, 259, 265, 272, 275, 279, 297, 307, 321, 335, 348, 366, 368, 370, 382, 388, 393, 410, 418, 419, 421, 426, 430, 452, 455, 456, 458, 464, 471, 478, 481, 488, 492, 495, 498, 502, 507, 516, 518, 520, 523, 529, 530, 542, 545, 550, 565, 574, 579, 580, 583, 587, 590, 600, 603, 621, 624, 628, 632, 643, 672, 695, 705, 713, 714, 719, 727, 728, 744, 754, 757, 761, 770, 786, 790, 805, 811, 817, 819, 837, 840, 841, 846, 860, 862, 864, 866, 875, 882, 887, 901, 916, 920, 925, 942, 957, 962, 964, 968, 991, 993, 994, 995, 998])
        self.assertEqual(response.json["collected"], [11, 14, 32, 38, 44, 55, 57, 58, 63, 83, 111, 144, 161, 194, 209, 219, 222, 236, 272, 276, 300, 315, 321, 322, 325, 348, 367, 385, 395, 397, 400, 413, 415, 442, 453, 461, 476, 477, 478, 490, 500, 527, 529, 533, 542, 560, 571, 588, 595, 604, 606, 629, 644, 678, 687, 700, 735, 750, 757, 760, 768, 779, 787, 817, 827, 840, 843, 844, 887, 901, 910, 911, 913, 915, 919, 921, 926, 933, 934, 944, 945, 982])
        self.assertEqual(response.json["posted"], [505, 532, 574, 632, 740, 972])
                 
if __name__ == '__main__':
    unittest.main()