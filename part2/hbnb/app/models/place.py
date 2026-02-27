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
        if not title:
            raise ValueError("Title is required")
        if len(title) > 100:
            raise ValueError("Title must be 100 characters or less")
        self.title = title

        self.description = description

        if not isinstance(price, (int, float)):
            raise ValueError("Price must be an integer or a float")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.price = price

        if not isinstance(latitude, (int, float)):
            raise ValueError("Latitude must be a number")
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self.latitude = latitude

        if not isinstance(longitude, (int, float)):
            raise ValueError("Longitude must be a number")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self.longitude = longitude

        if not isinstance(owner, User):
            raise ValueError("Owner must be a User instance")
        self.owner = owner

        self.reviews = []
        self.amenities = []

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
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """
        Add an amenity to the place.

        Args:
            amenity (Amenity): Amenity instance to associate with the place.

        Raises:
            ValueError: If amenity is not a valid Amenity instance.
        """
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be a Amenity instance")
        self.amenities.append(amenity)
