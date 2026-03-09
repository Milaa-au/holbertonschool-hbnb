#!/usr/bin/python3

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    """
    Class representing a review of a place by a user.

    Attributes:
        text (str): Text of the comment
        rating (int): Rating from 1 to 5
        place (Place): Place associated with the review
        user (User): User who wrote the review
    """

    def __init__(self, text, rating, place, user):
        """
        Initializes a new instance of Review.

        Args:
            text (str): Text of the comment
            rating (int): Rating from 1 to 5
            place (Place): Associated location
            user (User): Author of the review

        Raises:
            ValueError: if validations fail
        """
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
