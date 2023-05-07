from typing import List, Tuple

Placeholder = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"""
class to describe structure of a post
"""

class Post:
    def __init__(self, uid: int, posted_by: int, liked_by: List[int] = None, collected_by: List[int] = None, 
                 title: str = None, paragraph : List[str] = None, labels: List[str] = None, photo: str = None) -> None:
        # user id
        self.__uid = uid
        # list of user ids who have liked the post
        self.liked_by = liked_by 
        # list of user ids who have collected the post
        self.collected_by = collected_by
        # title of the post
        self.title = title
        # content of the post (list of strings)
        self.paragraph = paragraph
        # labels of the post; see labels in data_generator.py
        self.labels = labels
        # user id of poster
        self.__posted_by = posted_by
        # url
        self.photo = photo
    
    def get_val(self):
        return {"pid": int(self.__uid),
                "posted_by": int(self.__posted_by),
                "liked_by": self.liked_by,
                "collected_by": self.collected_by,
                "title": self.title,
                "paragraph": self.paragraph,
                "labels": self.labels,
                "photo": self.photo}

    