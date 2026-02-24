#!/usr/bin/python3
"""
Base model.

This module defines the BaseModel class, which provides common
attributes and behavior shared by all domain models such as
unique identification and timestamp management.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models.

    Provides a unique identifier and timestamps for creation
    and last update. Also includes helper methods to update
    and persist state changes.
    """
    def __init__(self):
        """
        Initialize a new BaseModel instance.

        Generates a unique UUID and sets creation and update
        timestamps to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Update the last modification timestamp.

        This method should be called whenever the object state
        changes to reflect the latest update time.
        """
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Update model attributes from a dictionary.

        Iterates over the provided key-value pairs and updates
        existing attributes only, then refreshes the update
        timestamp.

        Args:
            data (dict): Dictionary containing attributes to update.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
