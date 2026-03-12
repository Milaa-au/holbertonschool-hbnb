#!/usr/bin/python3
from app import db, bcrypt
import uuid
from .base_model import BaseModel 

class User(BaseModel):
     __tablename__ = 'users'

     first_name = db.Column(db.String(50), nullable=False)
     last_name = db.Column(db.String(50), nullable=False)
     email = db.Column(db.String(120), nullable=False, unique=True)
     password = db.Column(db.String(128), nullable=False)
     is_admin = db.Column(db.Boolean, default=False)

    def hash_password(self, password):
        """Hash the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    @validates('first_name')
    def validate_first_name(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("First name is required")
        if len(value) > 50:
            raise ValueError("First name must be 50 characters or less")
        return value

    @validates('last_name')
    def validate_last_name(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Last name is required")
        if len(value) > 50:
            raise ValueError("Last name must be 50 characters or less")
        return value
    
    @validates('email')
    def validate_email(self, key, value):
        if not isinstance(value, str):
            raise ValueError("Email is required")
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        return value

    @validates('is_admin')
    def validate_is_admin(self, key, value):
        if not isinstance(value, bool):
            raise TypeError("Is Admin must be a boolean")
        return value

    def add_place(self, place):
        """Add an amenity to the place."""
        self.places.append(place)

    def add_review(self, review):
        """Add an amenity to the place."""
        self.reviews.append(review)

    def delete_review(self, review):
        """Add an amenity to the place."""
        self.reviews.remove(review)
