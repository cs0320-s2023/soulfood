import unittest
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()

    # tests searching for user id
    # when the user id is less than 0
    def test_user_id_invalid(self):
        response = self.client.get('/search/-2')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, 'Invalid user id')
    # when the user with that id hasn't posted anything
    def test_user_id_absent(self):
        response = self.client.get('/search/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
    # when the user with that id has posted only once
    def test_user_id_once(self):
        response = self.client.get('search/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 
                         [{'uid': 220, 
                           'posted_by': 100, 
                           'liked_by': [129, 144, 169, 174, 157, 194, 131, 55, 53, 164, 160, 5, 95, 132, 76, 88, 125, 80], 
                           'collected_by': [103, 137, 153], 
                           'title': 'Sample Data:220', 
                           'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'], 
                           'labels': ['Labanese', 'Food therapy', 'Drinks are good', 'Best for birthday party', 'Fast serving', 'Clean environment', 'Best Ramen Place']}
                        ])
    # when the user with that id has posted multiple times
    def test_user_id_multiple(self):
        response = self.client.get('search/61')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {'uid': 23, 
             'posted_by': 61, 
             'liked_by': [11, 64, 10, 52, 28, 38, 13, 12, 43, 106, 115, 7, 45, 151, 9, 110, 84, 130, 26, 152, 93, 3, 23, 78, 29, 156, 162, 171, 19, 76, 65, 146, 105, 5, 200, 33, 191], 
             'collected_by': [41, 16, 141, 93, 67, 37, 149, 132, 13, 112, 64, 27, 62, 174, 32, 24, 144, 29, 157, 7, 195, 172, 101, 4, 150, 83, 56], 
             'title': 'Sample Data:23', 
             'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'],
             'labels': ['Spanish', 'Family made', 'Best for birthday party', 'Drinks are good', 'Best for small groups', 'Great servers']
             },
            {'uid': 41, 
             'posted_by': 61, 
             'liked_by': [189, 97, 28, 124, 117, 142, 123, 49, 55, 73, 186, 57, 195, 178, 17, 191, 138, 37, 106, 137, 94, 148, 23, 39, 140, 141, 147, 43, 65, 61, 82, 175], 
             'collected_by': [94, 48, 169, 76, 180, 130, 182, 165], 
             'title': 'Sample Data:41', 
             'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'], 
             'labels': ['Greek', 'Food therapy', 'Best for small groups', 'Clean environment']
             },
            {'uid': 47, 
             'posted_by': 61, 
             'liked_by': [133, 62, 65, 139, 22, 38, 80, 102, 130, 144, 99, 166, 17, 199, 48, 93, 129, 90, 85, 28, 169, 132, 106, 196, 127, 183, 61, 118, 44, 8, 11, 19, 115, 165, 146, 158, 68, 63, 43, 156, 175, 103, 195, 47], 
             'collected_by': [1, 195, 130, 94, 16, 167, 38, 21, 169, 117, 116, 91, 168, 128, 127, 70, 26, 27, 118, 153, 82, 48, 155, 99, 71, 111, 7, 36, 142], 
             'title': 'Sample Data:47', 
             'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'], 
             'labels': ['Mexican', 'Food story', 'Fast serving', 'Best for large groups', 'Best Ramen Place', 'Good for Dinner']
             },
            {'uid': 283, 
             'posted_by': 61, 
             'liked_by': [26, 20, 194, 124, 118, 104, 154, 161, 151, 46, 121, 117, 65, 126, 170, 27, 103, 180, 78, 134], 
             'collected_by': [169, 73, 53, 84, 127, 200, 52, 96, 147, 152, 4, 143, 104, 114, 70, 57, 12, 112, 81, 142], 
             'title': 'Sample Data:283', 
             'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'], 
             'labels': ['Mexican', 'Food therapy', 'Great music', 'Best for date', 'Drinks are good', 'Best for small groups']
             },
            {'uid': 299, 
             'posted_by': 61, 
             'liked_by': [193, 165, 32, 89, 173, 169, 138, 106, 167, 125, 80, 139, 36, 10, 178, 9, 23, 175, 151, 172, 78, 161, 96, 199, 166, 38, 42],
             'collected_by': [4, 53, 159, 18, 101, 19, 42, 78, 73, 79, 151, 178], 
             'title': 'Sample Data:299', 
             'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'], 
             'labels': ['Japanese', 'Food story', 'Great restaurant', 'Fast serving', 'Line is too long']
             },
            {'uid': 659, 
             'posted_by': 61, 
             'liked_by': [35, 48, 63, 58, 101, 57, 115, 38, 173, 71, 125, 156, 105, 23, 122, 106, 74, 165, 36, 90, 166, 59, 44, 138, 108, 10, 82, 195, 123, 4, 132, 5], 
             'collected_by': [126, 158, 170, 147, 97, 133], 
             'title': 'Sample Data:659', 
             'paragraph': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'], 
             'labels': ['Turkey', 'Family made', 'Great servers', 'Good for brunch', 'Good for Dinner']
             },
        ])


    # tests searching for keyword
    # when the keyword is empty
    def test_keyword_error(self):
        response = self.client.get('search/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, 'Keyword should not be empty')
    # when the keyword can't be found in any post
    def test_keyword_absent(self):
        response = self.client.get('search/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
    # when the keyword can be found in some posts
    def test_keyword_present(self):
        response = self.client.get('search/voluptate')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, [])