#!/usr/bin/python3
"""
User model.

This module defines the User entity which extends BaseModel and
represents an application user with validation rules for core fields.
"""


from app.models.base_model import BaseModel
import re


class User(BaseModel):
    """
    User domain model.

    Represents a user in the system with basic identity information
    and optional administrative privileges. Validation is performed
    during initialization to ensure data integrity.
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Initialize a new User instance.

        Validates required fields and constraints such as maximum
        length for names and basic email format.

        Args:
            first_name (str): User's first name (required, max 50 characters).
            last_name (str): User's last name (required, max 50 characters).
            email (str): User's email address (required, must be valid format).
            is_admin (bool, optional): Indicates whether the user has
                administrative privileges. Defaults to False.

        Raises:
            ValueError: If any required field is missing or invalid.
        """
        super().__init__()
        if not first_name:
            raise ValueError("First name is required")
        if len(first_name) > 50:
            raise ValueError("First name must be 50 characters or less")
        self.first_name = first_name

        if not last_name:
            raise ValueError("Last name is required")
        if len(last_name) > 50:
            raise ValueError("Last name must be 50 characters or less")
        self.last_name = last_name

        if not email:
            raise ValueError("Email is required")
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        self.email = email

        self.is_admin = is_admin
