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
        """create_user that create user"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """get_user that retrieved an user"""
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """get_all_users that retrieved all users"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """update_user that update an user"""
        user = self.get_user(user_id)
        if not user:
            return None
        self.user_repo.update(user_id, user_data)
        return self.get_user(user_id)

    def get_user_by_email(self, email):
        """get_user_by_email that retrieved an user via an email"""
        return self.user_repo.get_by_attribute('email', email)

    def create_place(self, place_data):
        """create_place that create place"""
        owner_id = place_data["owner_id"]
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError(("Owner not found"))

        place = Place(
            place_data["title"],
            place_data["description"],
            place_data["price"],
            place_data["latitude"],
            place_data["longitude"],
            owner
        )

        amenities_ids = place_data["amenities"]
        for amenity_id in amenities_ids:
            amenity = self.amenity_repo.get(amenity_id)

            if not amenity:
                raise ValueError(("Amenity not found"))

            place.add_amenity(amenity)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """get_place that retrieved place"""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """get_all_places that retrieved all places"""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """update_place that update a place"""
        place = self.get_place(place_id)
        if not place:
            return None
        if "owner_id" in place_data:
            raise ValueError("Owner cannot be modified")
        if "amenities" in place_data:
            raise ValueError("Amenities connot be modified")

        self.place_repo.update(place_id, place_data)
        return self.get_place(place_id)
