import unittest
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()

    # tests searching for posts by user id
    # when the user id is not given
    def test_post_uid_empty(self):
        response = self.client.get('/search/post/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.error, 'Keyword should not be empty')
    # when the user id is less than 0
    def test_post_uid_invalid(self):
        response = self.client.get('/search/post/-2')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, 'User id should be nonnegative')
    # when the user with that id hasn't posted anything
    def test_post_uid_absent(self):
        response = self.client.get('/search/post/0')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, 'This user has not posted anything yet.')
    # when the user with that id has posted only once
    def test_post_uid_once(self):
        response = self.client.get('search/post/198')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 
                         [{"pid": 358, 
                           "posted_by": 198, 
                           "liked_by": [179, 130, 152, 84, 118, 55, 56, 113, 166, 30, 106, 72, 111, 29, 27, 158, 185, 10, 188, 129, 48, 175, 196, 59, 2, 81, 128, 160, 68, 115, 197, 100, 49, 79, 28, 66, 24, 127, 31], 
                           "collected_by": [107, 124, 9, 59, 75, 70, 116], 
                           "title": "Sample Data:358", 
                           "paragraph": ["\"But what,\" said she, after a pause, \"can have been his motive?--what can have induced him to behave so cruelly?\""], 
                           "labels": ["Turkey", "Food story", "Fast serving", "Best for small groups"],
                           "photo": "https://images.pexels.com/photos/349610/pexels-photo-349610.jpeg"
                           }
                        ])
    # when the user with that id has posted multiple times
    def test_post_uid_multiple(self):
        response = self.client.get('search/post/199')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {"pid": 295, 
             "posted_by": 199, 
             "liked_by": [169, 15, 85, 120, 29, 138, 199, 136, 185, 57, 116, 12, 33, 1, 135, 193, 88, 134, 140, 74, 71, 184, 31, 142, 46, 167, 14, 22, 89, 58, 50], 
             "collected_by": [152, 200, 35, 175, 40, 88, 3, 127, 192, 13, 34, 168, 129, 60, 80, 185, 49, 61, 119], 
             "title": "Sample Data:295", 
             "paragraph": ["\"Oh! my dear,\" cried his wife, \"I cannot bear to hear that mentioned. Pray do not talk of that odious man. I do think it is the hardest thing in the world, that your estate should be entailed away from your own children; and I am sure if I had been you, I should have tried long ago to do something or other about it.\"", "Jane and Elizabeth attempted to explain to her the nature of an entail. They had often attempted it before, but it was a subject on which Mrs. Bennet was beyond the reach of reason; and she continued to rail bitterly against the cruelty of settling an estate away from a family of five daughters, in favour of a man whom nobody cared anything about."], 
             "labels": ["Indian", "Food therapy", "Best for birthday party", "Drinks are good", "Great music", "Best for date"], 
             "photo": "https://images.pexels.com/photos/8165305/pexels-photo-8165305.jpeg"
             },
            {"pid": 683, 
             "posted_by": 199,
             "liked_by": [143, 1, 163, 11, 75, 102, 92, 82, 4, 98, 23, 31, 152, 81, 27, 128, 103, 116, 130, 15, 28, 172, 160, 20, 176, 174, 39], 
             "collected_by": [8, 161, 191, 25, 164, 104, 184, 136, 141, 30, 93, 64, 28], 
             "title": "Sample Data:683", 
             "paragraph": ["Elizabeth was sitting by herself the next morning, and writing to Jane, while Mrs. Collins and Maria were gone on business into the village, when she was startled by a ring at the door, the certain signal of a visitor. As she had heard no carriage, she thought it not unlikely to be Lady Catherine, and under that apprehension was putting away her half-finished letter that she might escape all impertinent questions, when the door opened, and to her very great surprise, Mr. Darcy, and Mr. Darcy only, entered the room."], 
             "labels": ["Chinese", "Family made", "Line is too long", "Best for date", "Good for Dinner"], 
             "photo": "https://images.pexels.com/photos/1474157/pexels-photo-1474157.jpeg"
             },
            {"pid": 800, 
             "posted_by": 199, 
             "liked_by": [145, 94, 136, 104, 49, 95, 178, 189, 29, 13, 152, 37, 64, 162, 133, 169], 
             "collected_by": [181, 168, 12, 65, 42, 77, 28, 104, 140, 175, 58, 47, 39, 165, 50], 
             "title": "Sample Data:800", 
             "paragraph": ["\"They are going to be encamped near Brighton; and I do so want papa to take us all there for the summer! It would be such a delicious scheme, and I dare say would hardly cost any thing at all. Mamma would like to go too of all things! Only think what a miserable summer else we shall have!\""], 
             "labels": ["Chinese", "Food story", "Line is too long", "Best for birthday party"], 
             "photo": "https://images.pexels.com/photos/248509/pexels-photo-248509.jpeg"
             },
            {"pid": 979, 
             "posted_by": 199, 
             "liked_by": [127, 31, 21, 46, 118, 89, 85, 180, 67, 24, 149, 69, 115, 37, 93, 91, 173, 179, 133, 171, 33], 
             "collected_by": [64, 25, 109, 81, 40, 138, 74, 22, 126, 97, 82, 136, 29, 51], 
             "title": "Sample Data:979", 
             "paragraph": ["\"That is all settled;\" repeated the other, as she ran into her room to prepare. \"And are they upon such terms as for her to disclose the real truth! Oh, that I knew how it was!\""], 
             "labels": ["Greek", "Family made", "Great servers", "Best for large groups", "Best for small groups", "Best for date", "Good for lunch"], 
             "photo": "https://images.pexels.com/photos/884600/pexels-photo-884600.jpeg"
             },
        ])


if __name__ == '__main__':
    unittest.main()