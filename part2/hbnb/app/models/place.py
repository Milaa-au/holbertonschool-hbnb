#!/usr/bin/python3
"""
Place model.

This module defines the Place entity which represents a property
listed in the application. It includes location data, pricing,
ownership, and relationships with reviews and amenities.
"""


from app.models.base_model import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    """
    Place domain model.

    Represents a property that can be listed by a user. A place
    includes descriptive information, geographic coordinates,
    pricing, an owner, and collections of reviews and amenities.
    """

    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Initialize a new Place instance.

        Validates required fields, numeric ranges for coordinates,
        and ensures the owner is a valid User instance.

        Args:
            title (str): Name of the place (required, max 100 characters).
            description (str): Optional description of the place.
            price (float | int): Price per stay, must be greater than 0.
            latitude (float | int): Geographic latitude (-90 to 90).
            longitude (float | int): Geographic longitude (-180 to 180).
            owner (User): The user who owns the place.

        Raises:
            ValueError: If any field is missing or invalid.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title is required")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) > 100:
            raise ValueError("Title must be 100 characters or less")
        self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be an integer or a float")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if value is None or not isinstance(value, (int, float)):
            raise ValueError("Latitude must be a number")
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Longitude must be a number")
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self.__longitude = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("Owner must be a User instance")
        self.__owner = value

    def add_review(self, review):
        """
        Add a review to the place.

        Args:
            review (Review): Review instance to associate with the place.

        Raises:
            ValueError: If review is not a valid Review instance.
        """
        from app.models.review import Review

        if not isinstance(review, Review):
            raise ValueError("review must be a Review instance")
        if review not in self.reviews:
            self.reviews.append(review)

    def delete_review(self, review):
        """Add an amenity to the place."""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """
        Add an amenity to the place.

        Args:
            amenity (Amenity): Amenity instance to associate with the place.

        Raises:
            ValueError: If amenity is not a valid Amenity instance.
        """
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be an Amenity instance")
        if amenity not in self.amenities:
            self.amenities.append(amenity)

