from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not text:
            raise ValueError("text is required")
        self.text = text

        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.rating = rating

        if not isinstance(place, Place):
            raise ValueError("place must be a Place instance")
        self.place = place

        if not isinstance(user, User):
            raise ValueError("user must be a User instance")
        self.user = user
