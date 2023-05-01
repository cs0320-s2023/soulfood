from typing import List, Tuple

Placeholder = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

class Post:
    def __init__(self, uid: int, posted_by: int, liked_by: List[int] = None, collected_by: List[int] = None, 
                 title: str = None, paragraph : List[str] = None, labels: List[str] = None, photo: str = None) -> None:
        self.uid = uid
        self.liked_by = liked_by 
        self.collected_by = collected_by
        self.title = title
        self.paragraph = paragraph
        self.labels = labels
        self.posted_by = posted_by
        self.photo = photo
    
    def get_val(self):
        return {"pid": int(self.uid),
                "posted_by": int(self.posted_by),
                "liked_by": self.liked_by,
                "collected_by": self.collected_by,
                "title": self.title,
                "paragraph": self.paragraph,
                "labels": self.labels,
                "photo": self.photo}

    