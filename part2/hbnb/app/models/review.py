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
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("text is required")
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        self.__text = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise ValueError("Rating must be an integer")
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.__rating = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise ValueError("place must be a Place instance")
        self.__place = value

    @property
    def user(self):
        return self.__use

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("user must be a User instance")
        self.__user = value
