"""Facade is an intermediary between the API layer and
the persistance layer.
"""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place


class HBnBFacade:
    """HBnBFacade acts as an intermediary between the API layer and the
        persistence layer. It centralizes business logic and abstracts
        direct access to the repositories.
    """
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        Creates a new user.

        Args:
        user_data (dict): Dictionary containing user information.

        Returns:
        User: The created user object.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieves a user by their ID.

        Args:
        user_id (str): User ID.

        Returns:
        User: The corresponding user object or None if not found.
        """
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """
        Retrieves all users.

        Returns:
        list: List of all user objects.
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """
        Updates the information for an existing user.

        Args:
        user_id (str): ID of the user to update.
        user_data (dict): Dictionary of fields to update.

        Returns:
        User: The updated user object, or None if the user does not exist.
        """
        user = self.get_user(user_id)
        if not user:
            return None
        self.user_repo.update(user_id, user_data)
        return self.get_user(user_id)

    def get_user_by_email(self, email):
        """
        Retrieves a user from their email address.

        Args:
        email (str): The user's email address.

        Returns:
        User: The corresponding user object or None if not found.
        """
        return self.user_repo.get_by_attribute('email', email)

    def create_place(self, place_data):
        """
        Creates a new place with validation of required fields.

        Args:
        place_data (dict): Dictionary containing the place information.

        Raises:
        ValueError: If a required field is missing or invalid.

        Returns:
        Place: The created place object.
        """
        try:
            owner_id = place_data["owner_id"]
            title = place_data["title"]
            description = place_data.get("description")
            price = place_data["price"]
            latitude = place_data["latitude"]
            longitude = place_data["longitude"]
            amenities_ids = place_data.get("amenities", [])
        except KeyError as e:
            raise ValueError(f"Missing field: {str(e)}")

        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        place = Place(
            title,
            description,
            price,
            latitude,
            longitude,
            owner
        )

        for amenity_id in amenities_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if not amenity:
                raise ValueError("Amenity not found")
            place.add_amenity(amenity)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """
            Retrieves a place by its identifier.

        Args:
        place_id (str): Identifier of the place.

        Returns:
        Place: The corresponding place object or None if not found.
        """
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """
        Retrieves all existing locations.

        Returns:
        list: List of all location objects.
        """
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """
        Updates an existing place with validation of modified fields.

        Args:
        place_id (str): ID of the place to be updated.
        place_data (dict): Dictionary containing the fields to be updated.

        Raises:
        ValueError: If a value is invalid (price <= 0, 
        latitude/longitude out of bounds, invalid title).

        Returns:
        Place: The updated place object or None if the place does not exist.
        """
        place = self.get_place(place_id)
        if not place:
            return None

        place_data.pop("owner_id", None)
        place_data.pop("amenities", None)

        if "price" in place_data and place_data["price"] <= 0:
            raise ValueError("Price must be greater than 0")

        if "latitude" in place_data:
            if place_data["latitude"] < -90 or place_data["latitude"] > 90:
                raise ValueError("Latitude must be between -90 and 90")

        if "longitude" in place_data:
            if place_data["longitude"] < -180 or place_data["longitude"] > 180:
                raise ValueError("Longitude must be between -180 and 180")

        if "title" in place_data:
            if not place_data["title"] or len(place_data["title"]) > 100:
                raise ValueError("Invalid title")

        self.place_repo.update(place_id, place_data)
        return self.get_place(place_id)

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

    def create_review(self, review_data):
        """
        Create a new review after validating the data.

        This method validates the data provided, verifies
        the existence of the associated user and location,
        then creates and saves a new review.

        Args:
        review_data (dict): Review data containing
            text, rating, user_id, and place_id.

        Returns:
        Review: Instance of the review created.

        Raises:
        ValueError: If the data is invalid, if a required field
        is missing, or if the user or place
        does not exist.
        """
        if not review_data or not isinstance(review_data, dict):
            raise ValueError("Invalid review data")

        required_fields = ["text", "rating", "user_id", "place_id"]
        for field in required_fields:
            if field not in review_data:
                raise ValueError(f"{field} is required")

        if not review_data["text"].strip():
            raise ValueError("Review text cannot be empty")

        rating = review_data["rating"]
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5")

        user_id = review_data["user_id"]
        if user_id not in self.users:
            raise ValueError("User not found")

        place_id = review_data["place_id"]
        if place_id not in self.places:
            raise ValueError("Place not found")

        review = Review(**review_data)

        self.reviews[review.id] = review

        place = self.places[place_id]
        place.reviews.append(review)

        return review

    def get_review(self, review_id):
        """
        Retrieve a review by its ID.

        Args:
        review_id (int): Unique ID of the review.

        Returns:
        Review: Instance corresponding to the ID provided.

        Raises:
        ValueError: If the ID is invalid or if the
        review does not exist.
        """
        if not review_id or not isinstance(review_id, int):
            raise ValueError("Invalid review id")
        if review_id not in self.reviews:
            raise ValueError("Review not found")
        return self.reviews[review_id]

    def get_all_reviews(self):
        """
        Retrieve all saved reviews.

        Returns:
        list: List of all Review instances.
        """
        return Review.query.all()

    def get_reviews_by_place(self, place_id):
        """
        Retrieve all reviews associated with a given location.

        Args:
        place_id (str): Unique identifier for the location.

        Returns:
        list: List of reviews associated with the location.

        Raises:
        ValueError: If the location identifier is invalid
        or if the location does not exist.
        """
        if not place_id or not isinstance(place_id, str):
            raise ValueError("Invalid place id")
        if place_id not in self.places:
            raise ValueError("Place not found")
        filter_review = []
        for review in self.reviews.values():
            if review.place_id == place_id:
                filet_review.append(review)
        return filter_review

    def update_review(self, review_id, review_data):
        """
        Update an existing review.

        This method updates only the authorized fields
        of a review, then saves the changes to the database.
    

        Args:
        review_id (int): Unique identifier of the review.
        review_data (dict): Data to be modified.

        Returns:
        Review: Updated instance.

        Raises:
        ValueError: If the review does not exist.
        """
        review = Review.query.get(review_id)
    
        if not review:
            raise ValueError("Review not found")

        allowed_modif = ['text']

        for key, value in review_data.items():
            if key in allowed_modif:
                setattr(review, key, value)
            
        review.updated_at = datetime.utcnow()
        db.session.commit()
        return review

    def delete_review(self, review_id):
        """
        Delete an existing review.

        Args:
        review_id (int): Unique identifier of the review.

        Returns:
        bool: True if the deletion is successful.

        Raises:
        ValueError: If the review does not exist.
        """
        review = Review.query.get(review_id)
        if not review:
            raise ValueError("Review not found")
            
        db.session.delete(review)
        db.session.commit()

        return True
