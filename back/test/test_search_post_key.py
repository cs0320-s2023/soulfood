import unittest
import sys
sys.path.append('server')
import server
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
        self.assertEqual(response.json["error"], "Keyword should not be empty")
    # when the keyword can't be found in any post
    def test_keyword_absent(self):
        response = self.client.get('search/post/hello')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "The keyword is not found in any post.")
    # when the keyword can be found in a single post
    def test_keyword_once(self):
        response = self.client.get('search/post/blinds')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["pid"], 810)
        self.assertEqual(response.json[0]["posted_by"], 72)
        self.assertEqual(response.json[0]["liked_by"], [42, 169, 17, 93, 170, 152, 63, 92, 37, 161, 72, 26, 186, 35, 124, 127, 105, 153, 135, 175, 73, 147, 109, 82, 143, 59])
        self.assertEqual(response.json[0]["collected_by"], [171, 147, 79, 33, 125, 73, 105, 86, 112, 50, 200, 54, 184, 177, 187, 160, 106, 115, 161, 165, 107])
        self.assertEqual(response.json[0]["title"], "Sample Data:810")
        self.assertEqual(response.json[0]["paragraph"], ["\"Oh! Mary,\" said she, \"I wish you had gone with us, for we had such fun! as we went along, Kitty and me drew up all the blinds, and pretended there was nobody in the coach; and I should have gone so all the way, if Kitty had not been sick; and when we got to the George, I do think we behaved very handsomely, for we treated the other three with the nicest cold luncheon in the world, and if you would have gone, we would have treated you too. And then when we came away it was such fun! I thought we never should have got into the coach. I was ready to die of laughter. And then we were so merry all the way home! we talked and laughed so loud, that any body might have heard us ten miles off!\"",
                                                         "To this, Mary very gravely replied, \"Far be it from me, my dear sister, to depreciate such pleasures. They would doubtless be congenial with the generality of female minds. But I confess they would have no charms for _me_. I should infinitely prefer a book.\""])
        self.assertEqual(response.json[0]["labels"], ["Indian", "Family made", "Good for brunch", "Drinks are good", "Line is too long", "Great restaurant"])
        self.assertEqual(response.json[0]["photo"], "https://images.pexels.com/photos/1343465/pexels-photo-1343465.jpeg")
    # when the keyword can be found in multiple posts
    def test_keyword_multiple(self):
        response = self.client.get('search/post/proprietor')
        self.assertEqual(response.status_code, 200)
        # the first searched post
        self.assertEqual(response.json[0]["pid"], 338)
        self.assertEqual(response.json[0]["posted_by"], 150)
        self.assertEqual(response.json[0]["liked_by"], [169, 144, 186, 174, 108, 122, 64, 85, 29, 192, 168, 51, 127, 77, 105, 162, 
                                                        133, 151, 181, 113, 96, 87, 79, 112, 170, 172, 27, 140, 184, 178, 99, 84, 5, 72, 19])
        self.assertEqual(response.json[0]["collected_by"], [179, 40, 189, 160, 127, 70, 159, 165, 79, 153, 151, 197, 119])
        self.assertEqual(response.json[0]["title"], "Sample Data:338")
        self.assertEqual(response.json[0]["paragraph"], ["When this information was given, and they had all taken their seats, Mr. Collins was at leisure to look around him and admire, and he was so much struck with the size and furniture of the apartment, that he declared he might almost have supposed himself in the small summer breakfast parlour at Rosings; a comparison that did not at first convey much gratification; but when Mrs. Philips understood from him what Rosings was, and who was its proprietor, when she had listened to the description of only one of Lady Catherine\'s drawing-rooms, and found that the chimney-piece alone had cost eight hundred pounds, she felt all the force of the compliment, and would hardly have resented a comparison with the housekeeper\'s room.", "In describing to her all the grandeur of Lady Catherine and her mansion, with occasional digressions in praise of his own humble abode, and the improvements it was receiving, he was happily employed until the gentlemen joined them; and he found in Mrs. Philips a very attentive listener, whose opinion of his consequence increased with what she heard, and who was resolving to retail it all among her neighbours as soon as she could. To the girls, who could not listen to their cousin, and who had nothing to do but to wish for an instrument, and examine their own indifferent imitations of china on the mantle-piece, the interval of waiting appeared very long. It was over at last however. The gentlemen did approach; and when Mr. Wickham walked into the room, Elizabeth felt that she had neither been seeing him before, nor thinking of him since, with the smallest degree of unreasonable admiration. The officers of the ----shire were in general a very creditable, gentleman-like set, and the best of them were of the present party; but Mr. Wickham was as far beyond them all in person, countenance, air, and walk, as _they_ were superior to the broad-faced stuffy uncle Philips, breathing port wine, who followed them into the room."])
        self.assertEqual(response.json[0]["labels"], ["Mexican", "Food story", "Drinks are good", "Good for brunch", "Great music"])
        self.assertEqual(response.json[0]["photo"], "https://images.pexels.com/photos/784633/pexels-photo-784633.jpeg")
        # the second searched post
        self.assertEqual(response.json[1]["pid"], 877)
        self.assertEqual(response.json[1]["posted_by"], 166)
        self.assertEqual(response.json[1]["liked_by"], [51, 170, 41, 28, 164, 132, 61, 8, 119, 60, 187, 167, 183, 124, 101, 118, 134, 
                                                        166, 57, 94, 82, 79, 53, 162, 63, 13, 54, 136, 108, 14, 113, 19, 7, 62, 200, 
                                                        111, 38, 5, 133, 176, 198, 91, 190, 135, 50, 145, 87])
        self.assertEqual(response.json[1]["collected_by"], [197, 81, 140, 115, 107, 186, 132, 198, 176, 58, 151, 34, 175, 160, 20, 159, 133])
        self.assertEqual(response.json[1]["title"],  "Sample Data:877")
        self.assertEqual(response.json[1]["paragraph"], ["Accordingly, when she retired at night, she asked the chambermaid whether Pemberley were not a very fine place, what was the name of its proprietor, and with no little alarm, whether the family were down for the summer. A most welcome negative followed the last question--and her alarms being now removed, she was at leisure to feel a great deal of curiosity to see the house herself; and when the subject was revived the next morning, and she was again applied to, could readily answer, and with a proper air of indifference, that she had not really any dislike to the scheme.",
                                                         "To Pemberley, therefore, they were to go."])
        self.assertEqual(response.json[1]["labels"], ["Labanese", "Family made", "Great servers", "Fast serving", "Best for birthday party"])
        self.assertEqual(response.json[1]["photo"],  "https://images.pexels.com/photos/1414234/pexels-photo-1414234.jpeg")
        
if __name__ == '__main__':
    unittest.main()