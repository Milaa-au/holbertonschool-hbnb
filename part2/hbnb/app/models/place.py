#!/usr/bin/python3

from app.models.base_model import BaseModel

class Place(BaseModel):
    """
    Class representing a place (Place) in the HBnB system.

    Attributes:
        - title (str): Title or name of the place (max 100 characters).
        - description (str): Description of the place.
        - price (int | float): Price of the place, must be > 0.
        - latitude (float): Latitude of the place (-90 to 90).
        - longitude (float): Longitude of the place (-180 to 180).
        - owner (User): Owner of the place (instance of User).
        - reviews (list): List of reviews associated with the place.
        - amenities (list): List of amenities associated with the place.
    """

    def __init__(self, name, description, price, latitude, longitude):
        """
        Initializes a new instance of Place.

        Performs the following validations:
            - title must be non-empty and <= 100 characters
            - price must be an int or float and > 0
            - latitude must be between -90 and 90
            - longitude must be between -180 and 180
            - owner must be an instance of User
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
        Adds a review to the location.

        Args:
            review (Review): instance of Review to add

        Raises:
            ValueError: if the object is not an instance of Review
        """
        if not isinstance(review, Review):
            raise ValueError("review must be a Review instance")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """
        Adds an amenity to the location.

        Args:
            amenity (Amenity): instance of Amenity to add

        Raises:
            ValueError: if the object is not an instance of Amenity
        """
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be a Amenity instance")
        self.amenities.append(amenity)