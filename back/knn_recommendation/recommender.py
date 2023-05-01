# recommender.py
from load_data import data
from surprise import KNNWithMeans
from surprise import KNNWithMeans
from surprise import Dataset
from surprise.model_selection import GridSearchCV

# To use item-based cosine similarity
sim_options = {
    "name": "cosine",
    "user_based": False,  # Compute  similarities between items
}
algo = KNNWithMeans(sim_options=sim_options)