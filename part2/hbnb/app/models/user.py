#!/usr/bin/python3

from app.models.base_model import BaseModel

class User(BaseModel):
    """
    Class representing a user of the HBnB system.

    Attributes:
        first_name (str): User's first name (max 50 characters)
        last_name (str): User's last name (max 50 characters)
        email (str): User's email address, valid format required
        is_admin (bool): Indicates whether the user is an administrator (default False)
    """
    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Initializes a new instance of User.

        Performs the following validations:
            - first_name must be non-empty and ≤ 50 characters
            - last_name must be non-empty and ≤ 50 characters
            - email must be non-empty and have a valid format (contain ‘@’ and ‘.’)
            - is_admin is optional, default False
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
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        self.email = email

        self.is_admin = is_admin