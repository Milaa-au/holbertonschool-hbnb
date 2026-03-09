#!/usr/bin/python3

from app.models.base_model import BaseModel

class Amenity(BaseModel):
    """
    The Amenity class extends BaseModel, inheriting common attributes such as:
    id (UUID)
    created_at
    updated_at

    The constructor ensures data integrity 
    by validating the name attribute:
    It checks that a name is provided.
    It ensures the name does not exceed 50 characters.
    It raises a ValueError if validation fails.
    """

    def __init__(self, name):
        """
        This constructor initializes a new Amenity instance.
        It first calls the parent class constructor (BaseModel) 
        to initialize common attributes such as the unique 
        identifier and timestamps.
        Then, it validates the name parameter:
        It ensures that a name is provided. 
        If the name is missing or empty, a ValueError is raised.
        It checks that the name does not exceed 50 characters. 
        If it does, a ValueError is raised.
        If all validations pass, the name attribute is assigned to the instance.
        This guarantees that every Amenity object is created 
        with valid and consistent data.
        """
        super().__init__()

        if not name:
            raise ValueError("Name is required")

        if len(name) > 50:
            raise ValueError("Name must be 50 characters or less")

        self.name = name
