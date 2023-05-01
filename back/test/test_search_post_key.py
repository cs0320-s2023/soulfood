import unittest
import sys
sys.path.append('../server')
from server import app

class TestApp(unittest.TestCase):
    # setup
    def setUp(self):
        self.client = app.test_client()

    # tests searching for posts by keyword
    # when the keyword is empty
    def test_keyword_error(self):
        response = self.client.get('search/post/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, 'Keyword should not be empty')
    # when the keyword can't be found in any post
    def test_keyword_absent(self):
        response = self.client.get('search/post/hello')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'"The keyword is not found in any post."\n')
    # when the keyword can be found in a single post
    def test_keyword_once(self):
        response = self.client.get('search/post/blinds')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 
                         [
                             {"pid": 810, 
                              "posted_by": 72, 
                              "liked_by": [42, 169, 17, 93, 170, 152, 63, 92, 37, 161, 72, 26, 186, 35, 124, 127, 105, 153, 135, 175, 73, 147, 109, 82, 143, 59], 
                              "collected_by": [171, 147, 79, 33, 125, 73, 105, 86, 112, 50, 200, 54, 184, 177, 187, 160, 106, 115, 161, 165, 107], 
                              "title": "Sample Data:810", 
                              "paragraph": ["\"Oh! Mary,\" said she, \"I wish you had gone with us, for we had such fun! as we went along, Kitty and me drew up all the blinds, and pretended there was nobody in the coach; and I should have gone so all the way, if Kitty had not been sick; and when we got to the George, I do think we behaved very handsomely, for we treated the other three with the nicest cold luncheon in the world, and if you would have gone, we would have treated you too. And then when we came away it was such fun! I thought we never should have got into the coach. I was ready to die of laughter. And then we were so merry all the way home! we talked and laughed so loud, that any body might have heard us ten miles off!\"", "To this, Mary very gravely replied, \"Far be it from me, my dear sister, to depreciate such pleasures. They would doubtless be congenial with the generality of female minds. But I confess they would have no charms for _me_. I should infinitely prefer a book.\""], 
                              "labels": ["Indian", "Family made", "Good for brunch", "Drinks are good", "Line is too long", "Great restaurant"], 
                              "photo": "https://images.pexels.com/photos/1343465/pexels-photo-1343465.jpeg"
                              },
                         ])
    # when the keyword can be found in multiple posts
    def test_keyword_multiple(self):
        response = self.client.get('search/post/proprietor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 
                         [
                             {"pid": 338, 
                              "posted_by": 150, 
                              "liked_by": [169, 144, 186, 174, 108, 122, 64, 85, 29, 192, 168, 51, 127, 77, 105, 162, 133, 151, 181, 113, 96, 87, 79, 112, 170, 172, 27, 140, 184, 178, 99, 84, 5, 72, 19], 
                              "collected_by": [179, 40, 189, 160, 127, 70, 159, 165, 79, 153, 151, 197, 119], 
                              "title": "Sample Data:338", 
                              "paragraph": ["When this information was given, and they had all taken their seats, Mr. Collins was at leisure to look around him and admire, and he was so much struck with the size and furniture of the apartment, that he declared he might almost have supposed himself in the small summer breakfast parlour at Rosings; a comparison that did not at first convey much gratification; but when Mrs. Philips understood from him what Rosings was, and who was its proprietor, when she had listened to the description of only one of Lady Catherine's drawing-rooms, and found that the chimney-piece alone had cost eight hundred pounds, she felt all the force of the compliment, and would hardly have resented a comparison with the housekeeper's room.", "In describing to her all the grandeur of Lady Catherine and her mansion, with occasional digressions in praise of his own humble abode, and the improvements it was receiving, he was happily employed until the gentlemen joined them; and he found in Mrs. Philips a very attentive listener, whose opinion of his consequence increased with what she heard, and who was resolving to retail it all among her neighbours as soon as she could. To the girls, who could not listen to their cousin, and who had nothing to do but to wish for an instrument, and examine their own indifferent imitations of china on the mantle-piece, the interval of waiting appeared very long. It was over at last however. The gentlemen did approach; and when Mr. Wickham walked into the room, Elizabeth felt that she had neither been seeing him before, nor thinking of him since, with the smallest degree of unreasonable admiration. The officers of the ----shire were in general a very creditable, gentleman-like set, and the best of them were of the present party; but Mr. Wickham was as far beyond them all in person, countenance, air, and walk, as _they_ were superior to the broad-faced stuffy uncle Philips, breathing port wine, who followed them into the room."], 
                              "labels": ["Mexican", "Food story", "Drinks are good", "Good for brunch", "Great music"], 
                              "photo": "https://images.pexels.com/photos/784633/pexels-photo-784633.jpeg"
                              },
                            {"pid": 877, 
                             "posted_by": 166, 
                             "liked_by": [51, 170, 41, 28, 164, 132, 61, 8, 119, 60, 187, 167, 183, 124, 101, 118, 134, 166, 57, 94, 82, 79, 53, 162, 63, 13, 54, 136, 108, 14, 113, 19, 7, 62, 200, 111, 38, 5, 133, 176, 198, 91, 190, 135, 50, 145, 87], 
                             "collected_by": [197, 81, 140, 115, 107, 186, 132, 198, 176, 58, 151, 34, 175, 160, 20, 159, 133], 
                             "title": "Sample Data:877", 
                             "paragraph": ["Accordingly, when she retired at night, she asked the chambermaid whether Pemberley were not a very fine place, what was the name of its proprietor, and with no little alarm, whether the family were down for the summer. A most welcome negative followed the last question--and her alarms being now removed, she was at leisure to feel a great deal of curiosity to see the house herself; and when the subject was revived the next morning, and she was again applied to, could readily answer, and with a proper air of indifference, that she had not really any dislike to the scheme.", "To Pemberley, therefore, they were to go."],
                             "labels": ["Labanese", "Family made", "Great servers", "Fast serving", "Best for birthday party"], 
                             "photo": "https://images.pexels.com/photos/1414234/pexels-photo-1414234.jpeg"
                             },
                             {"pid": 888, 
                              "posted_by": 136, 
                              "liked_by": [161, 159, 188, 79, 53, 120, 24, 155, 138, 25, 16, 99, 146, 80, 150, 174, 2, 90, 10, 176, 68, 163, 8, 118, 137, 200, 157, 95, 172, 39, 123, 59, 54, 111, 97, 94, 109, 44, 70, 135, 21, 124, 36, 128, 153, 187, 154, 130], 
                              "collected_by": [92, 172, 136, 155, 164, 42, 82, 149, 151, 46, 147, 31, 183, 195, 41, 187], 
                              "title": "Sample Data:888", 
                              "paragraph": ["They descended the hill, crossed the bridge, and drove to the door; and, while examining the nearer aspect of the house, all her apprehensions of meeting its owner returned. She dreaded lest the chambermaid had been mistaken. On applying to see the place, they were admitted into the hall; and Elizabeth, as they waited for the housekeeper, had leisure to wonder at her being where she was.", "The housekeeper came; a respectable-looking, elderly woman, much less fine, and more civil, than she had any notion of finding her. They followed her into the dining-parlour. It was a large, well-proportioned room, handsomely fitted up. Elizabeth, after slightly surveying it, went to a window to enjoy its prospect. The hill, crowned with wood, from which they had descended, receiving increased abruptness from the distance, was a beautiful object. Every disposition of the ground was good; and she looked on the whole scene, the river, the trees scattered on its banks, and the winding of the valley, as far as she could trace it, with delight. As they passed into other rooms, these objects were taking different positions; but from every window there were beauties to be seen. The rooms were lofty and handsome, and their furniture suitable to the fortune of their proprietor; but Elizabeth saw, with admiration of his taste, that it was neither gaudy nor uselessly fine; with less of splendor, and more real elegance, than the furniture of Rosings."], 
                              "labels": ["Thai", "Family made", "Clean environment", "Good for Dinner"], 
                              "photo": "https://images.pexels.com/photos/2762930/pexels-photo-2762930.jpeg"
                              },
                         ])
        
if __name__ == '__main__':
    unittest.main()