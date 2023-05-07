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
        self.assertEqual(response.json["error"], 'Recommnedation cannot be given to unspecified user')

    # when num_recommend is not provided
    # when uid < 0
    def test_default_uid_negative(self):
        response = self.client.get('/recommend/-2/')
        self.assertEqual(response.status_code, 404)
        # self.assertEqual(response.json["error"], "User id should be nonnegative")
    # when uid is nonexistant
    def test_default_uid_invalid(self):
        response = self.client.get('/recommend/100000000/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "This user does not exist")
    # when uid is valid
    def test_default_uid_valid(self):
        response = self.client.get('/recommend/10/')
        self.assertEqual(response.status_code, 200)
        # the first recommended post
        self.assertEqual(response.json[0]["collected_by"], [89, 145, 85, 170, 132, 56, 91, 111, 59, 121, 178, 175, 57, 16, 51, 92, 193, 29, 122, 153, 26, 166, 108, 65, 50, 110, 169, 137, 60, 53])
        self.assertEqual(response.json[0]["labels"], ["French","Food story","Fast serving","Line is too long","Best Ramen Place"])
        self.assertEqual(response.json[0]["liked_by"], [99, 183, 12, 95, 93, 150, 193, 51, 37, 18, 136, 130, 60, 187, 90, 159, 175, 176, 122, 44, 39, 173, 33, 120, 174, 149, 141, 11, 66, 16, 54, 163, 111, 6, 29, 152, 103, 161, 114, 97, 134, 194, 179, 110, 43, 47, 48, 128, 184, "1"])
        self.assertEqual(response.json[0]["paragraph"], ["\"Do you know, mama, that my uncle Philips talks of turning away Richard, and if he does, Colonel Forster will hire him. My aunt told me so herself on Saturday. I shall walk to Meryton to-morrow to hear more about it, and to ask when Mr. Denny comes back from town.\""])
        self.assertEqual(response.json[0]["photo"], "https://images.pexels.com/photos/15141034/pexels-photo-15141034.jpeg")
        self.assertEqual(response.json[0]["pid"],  325)
        self.assertEqual(response.json[0]["posted_by"], 75)
        self.assertEqual(response.json[0]["title"], "Sample Data:325")
        # the second recommended post
        self.assertEqual(response.json[1]["collected_by"], [6, 75, 110, 65, 23, 143, 137, 44, 9, 151, 154, 108, 101, 142, 64, 5, 66, 67, 114, 57, 123, 28, 41, 170, 63, 153, 161])
        self.assertEqual(response.json[1]["labels"], ["Turkey","Family made","Best for large groups","Good for brunch","Line is too long"])
        self.assertEqual(response.json[1]["liked_by"], [127, 102, 17, 141, 97, 94, 140, 24, 9, 197, 43, 82, 193, 65, 77, 61, 198, 143, 103, 105, 29, 86, 199, 147, 18, 27, 16, 170, 89, 69, 167, 184, 185, 160, 36, 188, 154, 175, 153, 66, 136, 79, 194, 23, 151, 56, 156, 192, 96, "1"])
        self.assertEqual(response.json[1]["paragraph"], ["\"As much as I ever wish to be,\" cried Elizabeth warmly,--\"I have spent four days in the same house with him, and I think him very disagreeable.\"",
                                                         "\"I have no right to give _my_ opinion,\" said Wickham, \"as to his being agreeable or otherwise. I am not qualified to form one. I have known him too long and too well to be a fair judge. It is impossible for _me_ to be impartial. But I believe your opinion of him would in general astonish--and perhaps you would not express it quite so strongly anywhere else.--Here you are in your own family.\""])
        self.assertEqual(response.json[1]["photo"], "https://images.pexels.com/photos/1600711/pexels-photo-1600711.jpeg")
        self.assertEqual(response.json[1]["pid"], 345)
        self.assertEqual(response.json[1]["posted_by"],  112)
        self.assertEqual(response.json[1]["title"], "Sample Data:345")
        # third recommended psot
        self.assertEqual(response.json[2]["collected_by"], [158, 156, 169, 8, 198, 114, 112, 98, 174, 181, 77, 12, 91, 89, 103, 107, 153, 7, 60, 122, 71, 139, 191, 166, 154, 195])
        self.assertEqual(response.json[2]["labels"], ["Mexican","Food story","Best for date","Good for brunch","Best for small groups",
                           "Great restaurant","Good for lunch"])
        self.assertEqual(response.json[2]["liked_by"], [186, 9, 189, 143, 182, 62, 157, 50, 76, 150, 46, 67, 109, 103, 161, 110, 55, 146, 135, 57, 84, 2, 132, 152, 179, 4, 168, 121, 198, 166, 43, 33, 14, 11, 162, 15, 170, 61, 118, 81, 16, 91, 29, 140, 49, 101, 153, 107, 19, 54])
        self.assertEqual(response.json[2]["paragraph"], ["\"A man in distressed circumstances has not time for all those elegant decorums which other people may observe. If _she_ does not object to it, why should _we_?\"", 
                                                         "\"_Her_ not objecting, does not justify _him_. It only shews her being deficient in something herself--sense or feeling.\""])
        self.assertEqual(response.json[2]["photo"], "https://images.pexels.com/photos/3754296/pexels-photo-3754296.jpeg")
        self.assertEqual(response.json[2]["pid"], 600)
        self.assertEqual(response.json[2]["posted_by"], 98)
        self.assertEqual(response.json[2]["title"], "Sample Data:600")
         # the fourth recommended post
        self.assertEqual(response.json[3]["collected_by"], [112, 87, 144, 137, 95, 115, 45, 177, 17, 119, 138, 173, 105, 122, 158, 1, 167, 106, 13, 104, 47, 19, 133, 44, 121, 3, 156, 152, 166])
        self.assertEqual(response.json[3]["labels"], ["Chinese","Family made","Best for birthday party","Great music","Best for large groups",
                           "Great servers","Best for date"])
        self.assertEqual(response.jsonp[3]["liked_by"], [130, 146, 42, 192, 138, 190, 55, 119, 76, 134, 78, 10, 66, 115, 24, 194, 177, 117, 67, 49, 38, 143, 195, 9, 108, 79, 175, 121, 96, 135, 166, 128, 82, 16, 144, 57, 18, 101, 120, 35, 112, 60, 152, 142, 27, 185, 59, 116, 196, 6])
        self.assertEqual(response.json[3]["paragraph"], ["Elizabeth's mind was too full for conversation, but she saw and admired every remarkable spot and point of view. They gradually ascended for half a mile, and then found themselves at the top of a considerable eminence, where the wood ceased, and the eye was instantly caught by Pemberley House, situated on the opposite side of a valley, into which the road with some abruptness wound. It was a large, handsome, stone building, standing well on rising ground, and backed by a ridge of high woody hills;--and in front, a stream of some natural importance was swelled into greater, but without any artificial appearance. Its banks were neither formal, nor falsely adorned. Elizabeth was delighted. She had never seen a place for which nature had done more, or where natural beauty had been so little counteracted by an awkward taste. They were all of them warm in their admiration; and at that moment she felt, that to be mistress of Pemberley might be something!"])
        self.assertEqual(response.json[3]["photo"],  "https://images.pexels.com/photos/2894276/pexels-photo-2894276.jpeg")
        self.assertEqual(response.json[3]["pid"], 887)
        self.assertEqual(response.json[3]["posted_by"], 41)
        self.assertEqual(response.json[3]["title"], "Sample Data:887")
        # the fifth recommended post
        self.assertEqual(response.json[4]["collected_by"], [126, 9, 153, 78, 39, 93, 108, 139, 41, 136, 144, 176, 70, 190, 169, 135, 167, 196, 35, 123, 197, 161, 94, 183, 199, 134, 11])
        self.assertEqual(response.json[4]["labels"], ["French","Family made","Best for date","Great music","Good for lunch"])
        self.assertEqual(response.json[4]["liked_by"], [14, 113, 116, 91, 83, 7, 109, 187, 104, 73, 57, 127, 102, 161, 97, 170, 40, 131, 86, 176, 24, 55, 175, 169, 50, 145, 194, 48, 64, 200, 110, 84, 29, 195, 105, 129, 128, 101, 142, 96, 139, 137, 159, 68, 150, 1, 82, 26])
        self.assertEqual(response.json[4]["paragraph"], ["The conversation soon turned upon fishing, and she heard Mr. Darcy invite him, with the greatest civility, to fish there as often as he chose, while he continued in the neighbourhood, offering at the same time to supply him with fishing tackle, and pointing out those parts of the stream where there was usually most sport. Mrs. Gardiner, who was walking arm in arm with Elizabeth, gave her a look expressive of her wonder. Elizabeth said nothing, but it gratified her exceedingly; the compliment must be all for herself. Her astonishment, however, was extreme; and continually was she repeating, \"Why is he so altered? From what can it proceed? It cannot be for _me_, it cannot be for _my_ sake that his manners are thus softened. My reproofs at Hunsford could not work such a change as this. It is impossible that he should still love me.\"","After walking some time in this way, the two ladies in front, the two gentlemen behind, on resuming their places, after descending to the brink of the river for the better inspection of some curious water-plant, there chanced to be a little alteration. It originated in Mrs. Gardiner, who, fatigued by the exercise of the morning, found Elizabeth's arm inadequate to her support, and consequently preferred her husband's. Mr. Darcy took her place by her niece, and they walked on together. After a short silence, the lady first spoke. She wished him to know that she had been assured of his absence before she came to the place, and accordingly began by observing, that his arrival had been very unexpected--\"for your housekeeper,\" she added, \"informed us that you would certainly not be here till to-morrow; and indeed, before we left Bakewell, we understood that you were not immediately expected in the country.\" He acknowledged the truth of it all; and said that business with his steward had occasioned his coming forward a few hours before the rest of the party with whom he had been travelling. \"They will join me early to-morrow,\" he continued, \"and among them are some who will claim an acquaintance with you,--Mr. Bingley and his sisters.\""])
        self.assertEqual(response.json[4]["photo"], "https://images.pexels.com/photos/164504/pexels-photo-164504.jpeg")
        self.assertEqual(response.json[4]["pid"], 923)
        self.assertEqual(response.json[4]["posted_by"], 77)
        self.assertEqual(response.json[4]["title"], "Sample Data:923")
        
    # when num_recommend is provided
    # when uid < 0
    def test_uid_negative(self):
        response = self.client.get('/recommend/-1/20')
        self.assertEqual(response.status_code, 404)
        # self.assertEqual(response.json["error"], "User id should be nonnegative")
    # when uid is nonexistant
    def test_uid_invalid(self):
        response = self.client.get('/recommend/99999/10')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "This user does not exist")
    # when uid is valid
    def test_uid_valid(self):
        response = self.client.get('/recommend/190/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["collected_by"], [6, 75, 110, 65, 23, 143, 137, 44, 9, 151, 154, 108, 101, 142, 64, 5, 66, 67, 114, 57, 123, 28, 41, 170, 63, 153, 161])
        self.assertEqual(response.json[0]["labels"], ["Turkey","Family made","Best for large groups","Good for brunch","Line is too long" ])
        self.assertEqual(response.json[0]["liked_by"], [127, 102, 17, 141, 97, 94, 140, 24, 9, 197, 43, 82, 193, 65, 77, 61, 198, 143, 103, 105, 29, 86, 199, 147, 18, 27, 16, 170, 89, 69, 167, 184, 185, 160, 36, 188, 154, 175, 153, 66, 136, 79, 194, 23, 151, 56, 156, 192, 96, "1"])
        self.assertEqual(response.json[0]["paragraph"], ["\"As much as I ever wish to be,\" cried Elizabeth warmly,--\"I have spent four days in the same house with him, and I think him very disagreeable.\"","\"I have no right to give _my_ opinion,\" said Wickham, \"as to his being agreeable or otherwise. I am not qualified to form one. I have known him too long and too well to be a fair judge. It is impossible for _me_ to be impartial. But I believe your opinion of him would in general astonish--and perhaps you would not express it quite so strongly anywhere else.--Here you are in your own family.\""])
        self.assertEqual(response.json[0]["photo"], "https://images.pexels.com/photos/1600711/pexels-photo-1600711.jpeg")
        self.assertEqual(response.json[0]["pid"], 345)
        self.assertEqual(response.json[0]["posted_by"], 112)
        self.assertEqual(response.json[0]["title"], "Sample Data:345")
        # the second recommended post
        self.assertEqual(response.json[1]["collected_by"], [103, 46, 115, 66, 91, 49, 182, 64, 165, 194, 150, 6, 17, 56, 130, 63, 16, 158, 94, 181, 48, 44, 83, 19, 28, 152, 33])
        self.assertEqual(response.json[1]["labels"], [ "Spanish", "Family made", "Good for lunch", "Great servers", "Best for birthday party"])
        self.assertEqual(response.json[1]["liked_by"], [200, 7, 130, 9, 144, 102, 125, 129, 164, 23, 52, 18, 120, 31, 185, 195, 162, 160, 55, 82, 187, 32, 171, 126, 47, 141, 139, 71, 66, 101, 194, 136, 119, 177, 72, 183, 128, 169, 106, 77, 70, 165, 48, 140, 36, 151, 182])
        self.assertEqual(response.json[1]["paragraph"], ["\"A little sea-bathing would set me up for ever.\""])
        self.assertEqual(response.json[1]["photo"], "https://images.pexels.com/photos/428124/pexels-photo-428124.jpeg")
        self.assertEqual(response.json[1]["pid"], 845)
        self.assertEqual(response.json[1]["posted_by"], 133)
        self.assertEqual(response.json[1]["title"], "Sample Data:845")
        # the third recommended post
        self.assertEqual(response.json[2]["collected_by"], [112, 87, 144, 137, 95, 115, 45, 177, 17, 119, 138, 173, 105, 122, 158, 1, 167, 106, 13, 104, 47, 19, 133, 44, 121, 3, 156, 152, 166])
        self.assertEqual(response.json[2]["labels"], ["Chinese","Family made","Best for birthday party","Great music","Best for large groups","Great servers","Best for date"])
        self.assertEqual(response.json[2]["liked_by"], [130, 146, 42, 192, 138, 190, 55, 119, 76, 134, 78, 10, 66, 115, 24, 194, 177, 117, 67, 49, 38, 143, 195, 9, 108, 79, 175, 121, 96, 135, 166, 128, 82, 16, 144, 57, 18, 101, 120, 35, 112, 60, 152, 142, 27, 185, 59, 116, 196 ,6])
        self.assertEqual(response.json[2]["paragraph"], ["Elizabeth's mind was too full for conversation, but she saw and admired every remarkable spot and point of view. They gradually ascended for half a mile, and then found themselves at the top of a considerable eminence, where the wood ceased, and the eye was instantly caught by Pemberley House, situated on the opposite side of a valley, into which the road with some abruptness wound. It was a large, handsome, stone building, standing well on rising ground, and backed by a ridge of high woody hills;--and in front, a stream of some natural importance was swelled into greater, but without any artificial appearance. Its banks were neither formal, nor falsely adorned. Elizabeth was delighted. She had never seen a place for which nature had done more, or where natural beauty had been so little counteracted by an awkward taste. They were all of them warm in their admiration; and at that moment she felt, that to be mistress of Pemberley might be something!"])
        self.assertEqual(response.json[2]["photo"], "https://images.pexels.com/photos/2894276/pexels-photo-2894276.jpeg")
        self.assertEqual(response.json[2]["pid"], 887)
        self.assertEqual(response.json[2]["posted_by"], 41)
        self.assertEqual(response.json[2]["title"], "Sample Data:887")

if __name__ == '__main__':
    unittest.main()

