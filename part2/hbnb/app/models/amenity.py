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

        def create_amenity(self, amenity_data):
            """
            Creates a new Amenity instance after
            validating the data provided.

            This method checks that the
            data entered is valid and contains the
            required fields before creating
            a new Amenity object. If the data
            is invalid or if required information
            is missing, a ValueError error is raised.

            Once validated, the Amenity instance
            is instantiated and stored in the
            internal amenities collection, then returned.
            """

            if not amenity_data or not isinstance(amenity_data, dict):
                raise ValueError("Invalid amenity data")
            if "name" not in amenity_data or not amenity_data["name"]:
                raise ValueError("Amenity name is required")
            
            amenity = Amenity(**amenity_data)
            self.amenities[amenity.id] = amenity
            return amenity

        def get_amenity(self, amenity_id):

            """
            Retrieves a commodity from its identifier.

            Verifies that the identifier is valid and exists in
            memory storage before returning the corresponding object.
            """

            if not amenity_id or not isinstance(amenity_id, int):
                raise ValueError("Invalid amenity id")
            if amenity_id not in self.amenities:
                raise ValueError("Amenity not found")
            return self.amenities[amenity_id]

        def get_all_amenities(self):
            """
            Retrieves all amenities stored in the database.

            Performs a query to return all
            Amenity objects present in the database.
            """
            return Amenity.query.all()

        def update_amenity(self, amenity_id, amenity_data):
            """
            Updates an existing convenience.

            Searches for the convenience by its identifier, updates its
            attributes with the provided data, then saves the
            changes to the database.
            """
            amenity = Amenity.query.get(amenity_id)
    
            if not amenity:
            raise ValueError("Amenity not found")

            for key, value in amenity_data.items():
            setattr(amenity, key, value)

            db.session.commit()
            return amenity