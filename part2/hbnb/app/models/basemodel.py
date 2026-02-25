#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:

    """
    Base class for all entities in the system.

    Attributes:
        id (str): Unique identifier for the object (UUID).
        created_at (datetime): Date and time when
        the object was created.
        updated_at (datetime): Date and time of
        the last update to the object.
    """

    def __init__(self):

        """
        Initializes a new instance of BaseModel.

        - Generates a unique identifier (UUID) for the object.
        - Sets created_at and updated_at to the current time.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):

        """
        Updates the updated_at attribute to the current time.

        This method must be called each time the object is modified
        to reflect the latest update.
        """

        self.updated_at = datetime.now()

    def update(self, data):

        """
        Updates the object's attributes from a dictionary.

        Args:
            data (dict): Dictionary containing 
            the attributes to be updated
            and their new values.

        Notes:
            - Protected fields (‘id’, ‘created_at’) cannot be modified.
            - After the update, the save() method is automatically called
              to update updated_at.
        """

        protected_fields = {"id", "created_at"}

        for key, value in data.items():
            if hasattr(self, key) and key not in protected_fields:
                setattr(self, key, value)

        self.save()