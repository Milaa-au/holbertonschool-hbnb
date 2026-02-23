from app.models.base_model import BaseModel
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
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
        if not isinstance(review, Review):
            raise ValueError("review must be a Review instance")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be a Amenity instance")
        self.amenities.append(amenity)
