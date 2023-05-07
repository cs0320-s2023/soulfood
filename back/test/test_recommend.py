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
        self.assertEqual(response.json[0]["collected_by"], [171,103,185,159,140])
        self.assertEqual(response.json[0]["labels"], ["Japanese","Food story","Best for large groups","Great servers","Drinks are good","Great music"])
        self.assertEqual(response.json[0]["liked_by"], [117,34,63,57, 65,10,109,78,95,146,40,124,169,17,181,120,193,4,200])
        self.assertEqual(response.json[0]["paragraph"], ["\"Yes, indeed, and received no inconsiderable pleasure from the sight. Do you often dance at St. James's?\"",
      "\"Never, sir.\""])
        self.assertEqual(response.json[0]["photo"], "https://images.pexels.com/photos/1586942/pexels-photo-1586942.jpeg")
        self.assertEqual(response.json[0]["pid"],  103)
        self.assertEqual(response.json[0]["posted_by"], 10)
        self.assertEqual(response.json[0]["title"], "Sample Data:103")
        # the second recommended post
        self.assertEqual(response.json[1]["collected_by"], [69,7,76,95,133,183,10,33,13,125,23,195,120,4,54,173,28,
                                                            135,164,168,34,32,115,15,27,5,123,39,81])
        self.assertEqual(response.json[1]["labels"], ["French","Food story","Great music","Drinks are good","Clean environment"])
        self.assertEqual(response.json[1]["liked_by"], [197,160,10,178,71,14,171,8,66,186,68,61,116,67])
        self.assertEqual(response.json[1]["paragraph"], ["\"About a month,\" said Elizabeth; and then, unwilling to let the subject drop, added, \"He is a man of very large property in Derbyshire, I understand.\"",
      "\"Yes,\" replied Wickham;--\"his estate there is a noble one. A clear ten thousand per annum. You could not have met with a person more capable of giving you certain information on that head than myself--for I have been connected with his family in a particular manner from my infancy.\""])
        self.assertEqual(response.json[1]["photo"], "https://images.pexels.com/photos/769289/pexels-photo-769289.jpeg")
        self.assertEqual(response.json[1]["pid"], 343)
        self.assertEqual(response.json[1]["posted_by"],  106)
        self.assertEqual(response.json[1]["title"], "Sample Data:343")
        # third recommended psot
        self.assertEqual(response.json[2]["collected_by"], [55,132,198,185, 111,87,10,139,39,18,45,84])
        self.assertEqual(response.json[2]["labels"], ["Turkey","Family made","Drinks are good","Best for date","Great restaurant",
                                                      "Best for large groups","Great servers"])
        self.assertEqual(response.json[2]["liked_by"], [54,27,79,184, 46,11,48,82,8,106,124,31,12,109,187,172,190,60,
                                                        20,167,83,10,86,45,17])
        self.assertEqual(response.json[2]["paragraph"], ["\"Of music! Then pray speak aloud. It is of all subjects my delight. I must have my share in the conversation, if you are speaking of music. There are few people in England, I suppose, who have more true enjoyment of music than myself, or a better natural taste. If I had ever learnt, I should have been a great proficient. And so would Anne, if her health had allowed her to apply. I am confident that she would have performed delightfully. How does Georgiana get on, Darcy?\"",
      "Mr. Darcy spoke with affectionate praise of his sister's proficiency."])
        self.assertEqual(response.json[2]["photo"],"https://images.pexels.com/photos/349608/pexels-photo-349608.jpeg")
        self.assertEqual(response.json[2]["pid"], 665)
        self.assertEqual(response.json[2]["posted_by"], 85)
        self.assertEqual(response.json[2]["title"], "Sample Data:665")
         # the fourth recommended post
        self.assertEqual(response.json[3]["collected_by"], [138,58,10,95,59,83,14,102,18,2,187,96,17,80,49,173,68,57])
        self.assertEqual(response.json[3]["labels"], ["Spanish","Family made","Fast serving","Best for date","Good for lunch"])
        self.assertEqual(response.json[3]["liked_by"], [28,5,14,148,42,185,199,109,10,33,139,39,96,200,43,40])
        self.assertEqual(response.json[3]["paragraph"], ["\"Oh! no, my regret and compassion are all done away by seeing you so full of both. I know you will do him such ample justice, that I am growing every moment more unconcerned and indifferent. Your profusion makes me saving; and if you lament over him much longer, my heart will be as light as a feather.\"",
      "\"Poor Wickham; there is such an expression of goodness in his countenance! such an openness and gentleness in his manner.\""])
        self.assertEqual(response.json[3]["photo"],  "https://images.pexels.com/photos/1813466/pexels-photo-1813466.jpeg")
        self.assertEqual(response.json[3]["pid"], 823)
        self.assertEqual(response.json[3]["posted_by"], 160)
        self.assertEqual(response.json[3]["title"], "Sample Data:823")
        # the fifth recommended post
        self.assertEqual(response.json[4]["collected_by"], [16,182,172,72,198,132,126,196,56,160,111,33,153])
        self.assertEqual(response.json[4]["labels"], ["American","Food therapy","Good for Dinner","Great servers"])
        self.assertEqual(response.json[4]["liked_by"], [130,69,10,42,92,156,162,140,80,73,183,138,136,169,200,164,148,
                                                        184,141,39,24,121,161,117,41,55,67,32,66,89,31,20])
        self.assertEqual(response.json[4]["paragraph"], ["\"Good God! what is the matter?\" cried he, with more feeling than politeness; then recollecting himself, \"I will not detain you a minute, but let me, or let the servant, go after Mr. and Mrs. Gardiner. You are not well enough;--you cannot go yourself.\"",
      "Elizabeth hesitated, but her knees trembled under her, and she felt how little would be gained by her attempting to pursue them. Calling back the servant, therefore, she commissioned him, though in so breathless an accent as made her almost unintelligible, to fetch his master and mistress home, instantly."])
        self.assertEqual(response.json[4]["photo"], "https://images.pexels.com/photos/1309593/pexels-photo-1309593.jpeg")
        self.assertEqual(response.json[4]["pid"], 964)
        self.assertEqual(response.json[4]["posted_by"], 10)
        self.assertEqual(response.json[4]["title"], "Sample Data:964")
        
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
        self.assertEqual(response.json[0]["collected_by"], [28,32,106,102,84,36,190, 71, 50, 62, 170, 17, 72, 138, 63,
                                                            134,130,  155,195,176,66,1])
        self.assertEqual(response.json[0]["labels"], ["American","Food story","Great music","Best Ramen Place","Good for Dinner","Good for brunch","Best for small groups" ])
        self.assertEqual(response.json[0]["liked_by"], [81,55,53,174, 4, 118, 39, 131, 193, 6, 5, 114, 57, 64, 94,
                                                         73,158,  83,8,147,173,87])
        self.assertEqual(response.json[0]["paragraph"], ["Mr. Wickham's society was of material service in dispelling the gloom, which the late perverse occurrences had thrown on many of the Longbourn family. They saw him often, and to his other recommendations was now added that of general unreserve. The whole of what Elizabeth had already heard, his claims on Mr. Darcy, and all that he had suffered from him, was now openly acknowledged and publicly canvassed; and every body was pleased to think how much they had always disliked Mr. Darcy before they had known any thing of the matter."])
        self.assertEqual(response.json[0]["photo"], "https://images.pexels.com/photos/1556707/pexels-photo-1556707.jpeg")
        self.assertEqual(response.json[0]["pid"], 553)
        self.assertEqual(response.json[0]["posted_by"], 190)
        self.assertEqual(response.json[0]["title"], "Sample Data:553")
        # the second recommended post
        self.assertEqual(response.json[1]["collected_by"], [13,190,71,148,74,52,181,86,153,125,30,113,197,10, 155,
                                                            11,112,36,59])
        self.assertEqual(response.json[1]["labels"], [ "American","Family made","Good for brunch","Best for birthday party","Good for Dinner",
                                                       "Fast serving","Best for small groups"])
        self.assertEqual(response.json[1]["liked_by"], [31,11,163,112,40,24,190,138,7, 167, 126,170,103,200])
        self.assertEqual(response.json[1]["paragraph"], ["That the Miss Lucases and the Miss Bennets should meet to talk over a ball was absolutely necessary; and the morning after the assembly brought the former to Longbourn to hear and to communicate.",
      "\"_You_ began the evening well, Charlotte,\" said Mrs. Bennet with civil self-command to Miss Lucas. \"_You_ were Mr. Bingley's first choice.\""])
        self.assertEqual(response.json[1]["photo"], "https://images.pexels.com/photos/1813505/pexels-photo-1813505.jpeg")
        self.assertEqual(response.json[1]["pid"], 71)
        self.assertEqual(response.json[1]["posted_by"], 28)
        self.assertEqual(response.json[1]["title"], "Sample Data:71")
        # the third recommended post
        self.assertEqual(response.json[2]["collected_by"], [146,57,193,29,43,172,134,34,36,40,182,98,104,136,123,118,
                                                            142,1,79,188,97,122,114,178,27,65,107,158])
        self.assertEqual(response.json[2]["labels"], ["French","Food therapy","Good for brunch","Best Ramen Place"])
        self.assertEqual(response.json[2]["liked_by"], [108,28,116,38,74,78,59,118,20,61,60,8,166,58,14,24,107,163,99,
                                                        2,135,159,37,71,193,103,133,179,44,168,77,62,161,190,140,178])
        self.assertEqual(response.json[2]["paragraph"], ["In seeing Bingley, her thoughts naturally flew to her sister; and oh! how ardently did she long to know, whether any of his were directed in a like manner. Sometimes she could fancy, that he talked less than on former occasions, and once or twice pleased herself with the notion that as he looked at her, he was trying to trace a resemblance. But, though this might be imaginary, she could not be deceived as to his behaviour to Miss Darcy, who had been set up as a rival of Jane. No look appeared on either side that spoke particular regard. Nothing occurred between them that could justify the hopes of his sister. On this point she was soon satisfied; and two or three little circumstances occurred ere they parted, which, in her anxious interpretation, denoted a recollection of Jane, not untinctured by tenderness, and a wish of saying more that might lead to the mention of her, had he dared. He observed to her, at a moment when the others were talking together, and in a tone which had something of real regret, that it \"was a very long time since he had had the pleasure of seeing her;\" and, before she could reply, he added, \"It is above eight months. We have not met since the 26th of November, when we were all dancing together at Netherfield.\"",
      "Elizabeth was pleased to find his memory so exact; and he afterwards took occasion to ask her, when unattended to by any of the rest, whether _all_ her sisters were at Longbourn. There was not much in the question, nor in the preceding remark, but there was a look and a manner which gave them meaning."])
        self.assertEqual(response.json[2]["photo"],"https://images.pexels.com/photos/3713892/pexels-photo-3713892.jpeg")
        self.assertEqual(response.json[2]["pid"], 940)
        self.assertEqual(response.json[2]["posted_by"],190)
        self.assertEqual(response.json[2]["title"], "Sample Data:940")

if __name__ == '__main__':
    unittest.main()

