from load_data import data
from recommender import algo

# Computing the cosine similarity matrix...
# Done computing similarity matrix.
# <surprise.prediction_algorithms.knns.KNNWithMeans object at 0x7f04fec56898>

# user, item
# prediction = algo.predict(31, 2)
# prediction.est
# print(prediction)
# print(prediction.est)

"""
:param user_id: user id of user that wants a recommendation
:param number_of_recommendation: specifies the number of recommendations the user wants; these are the 'top' options for the user
:return: top number_of_recommendation recommendations for user
"""

def get_recommendation(user_id, number_of_recommendation = 5):
    trainingSet = data.build_full_trainset()
    algo.fit(trainingSet)  
    predictions = []
    for p in range(1, 1001):
        pre = algo.predict(user_id, p).est
        # print(pre)
        predictions.append((p, pre))
    return sorted(predictions, key = lambda prediction: prediction[1], reverse = True)[0:number_of_recommendation]

# print(get_recommendation(190, 10))
    