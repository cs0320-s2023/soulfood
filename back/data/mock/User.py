from typing import List, Tuple
from mock.Post import Post

Placeholder = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"""
class to describe structure of a post
"""

class User:
    def __init__(self, uid: int, id: str, bio: str = None, following: List[int] = None, followed_by: List[int] = None,
                 liked: List[int] = None, collected: List[int] = None, posted: List[int] = None) -> None:
        # user id
        self.uid = uid
        self.id = id
        # user bio
        self.bio = bio
        # list of user ids of who this user is following
        self.following = following 
        # list of user ids of who this user is followed by
        self.followed_by = followed_by
        # list of post numbers that this user has liked
        self.liked = liked
        self.collected = collected
        # list of post numbers this user has posted
        self.posted = posted

    def get_val(self):
        return {"uid": self.uid,
                "id": self.id,
                "bio": self.bio,
                "following": self.following,
                "followed_by": self.followed_by,
                "liked": self.liked,
                "collected": self.collected,
                "posted": self.posted}