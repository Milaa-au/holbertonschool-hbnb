#!/usr/bin/python3
"""
Review model.

This module defines the Review entity which represents a user's
evaluation of a place, including textual feedback and a numeric rating.
"""


from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    """
    Review domain model.

    Represents a review left by a user for a specific place.
    A review contains a text comment, a rating between 1 and 5,
    and references to the related user and place.
    """

    def __init__(self, text, rating, place, user):
        """
        Initialize a new Review instance.

        Performs validation on the review content, rating range,
        and ensures that associated objects are valid instances.

        Args:
            text (str): The review content. Must not be empty.
            rating (int): Numeric score between 1 and 5.
            place (Place): The place being reviewed.
            user (User): The user who created the review.

        Raises:
            ValueError: If text is missing, rating is invalid,
                or place/user are not valid instances.
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
