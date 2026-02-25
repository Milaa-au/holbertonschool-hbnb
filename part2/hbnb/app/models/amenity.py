#!/usr/bin/python3
"""
Amenity model.

This module defines the Amenity entity which represents a feature
or service that can be associated with a place (e.g., Wi-Fi, pool).
"""


from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity domain model.

    Represents a single amenity that can be attached to a place.
    Each amenity has a name with validation constraints.
    """

    def __init__(self, name):
        """
        Initialize a new Amenity instance.

        Validates that the name is provided and within the
        allowed length limit.

        Args:
            name (str): Name of the amenity (required, max 50 characters).

        Raises:
            ValueError: If name is missing or exceeds length constraints.
        """
        super().__init__()
        if not name:
            raise ValueError("Name is required")
        if len(name) > 50:
            raise ValueError("Name must be 50 characters or less")
        self.name = name
