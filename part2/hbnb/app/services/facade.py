#!/usr/bin/python3

from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

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
            """Create a new assessment with prior validation."""
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

        def get_amenity(self, amenity_id):

        def get_review(self, review_id):
            # Placeholder for logic to retrieve a review by ID
            pass

        def get_all_reviews(self):
            # Placeholder for logic to retrieve all reviews
            pass

        def get_reviews_by_place(self, place_id):
            # Placeholder for logic to retrieve all reviews for a specific place
            pass

        def update_review(self, review_id, review_data):
            # Placeholder for logic to update a review
            pass

        def delete_review(self, review_id):
            # Placeholder for logic to delete a review
            pass