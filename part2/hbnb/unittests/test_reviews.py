#!/usr/bin/python3
"""
Unit tests for Review endpoints of the Holberton HBNB project.
Covers creation, retrieval, update, and deletion of reviews,
including validation and error handling.
"""

import unittest
import uuid
from app import create_app
from app.services import facade


class TestReviewEndpoints(unittest.TestCase):
    """Test class for Review endpoints"""

    def setUp(self):
        """Set up a clean test environment before each test"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

        # Clear storage by resetting dictionaries
        facade.user_repo.storage = {}
        facade.place_repo.storage = {}
        facade.review_repo.storage = {}
        facade.amenity_repo.storage = {}

    def create_test_user(self):
        """Helper to create a user"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": f"john{uuid.uuid4()}@example.com"
        })
        self.assertEqual(response.status_code, 201)
        return response.get_json()["id"]

    def create_test_place(self, owner_id):
        """Helper to create a place"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Test Place",
            "description": "Nice place",
            "price": 100,
            "latitude": 45,
            "longitude": 3,
            "owner_id": owner_id,
            "amenities": []
        })
        self.assertEqual(response.status_code, 201)
        return response.get_json()["id"]

    def create_review_payload(self, user_id, place_id, rating=5, text="Great place"):
        """Helper to generate a review payload"""
        return {
            "text": text,
            "rating": rating,
            "user_id": user_id,
            "place_id": place_id
        }

    def test_create_review_valid(self):
        """Test creating a valid review"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        response = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id)
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["text"], "Great place")

    def test_create_review_invalid_rating(self):
        """Test creating a review with invalid rating"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        response = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id, rating=10)
        )
        self.assertEqual(response.status_code, 400)

    def test_create_review_empty_text(self):
        """Test creating a review with empty text"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        response = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id, text="")
        )
        self.assertEqual(response.status_code, 400)

    def test_create_review_invalid_user_or_place(self):
        """Test creating a review with invalid user or place"""
        response = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload("invalid-user", "invalid-place")
        )
        self.assertEqual(response.status_code, 400)

    def test_get_review_by_id_valid(self):
        """Test retrieving a review by valid ID"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        review_id = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id)
        ).get_json()["id"]

        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], review_id)

    def test_get_review_not_found(self):
        """Test retrieving a non-existent review"""
        response = self.client.get('/api/v1/reviews/nonexistent-id')
        self.assertEqual(response.status_code, 404)

    def test_get_all_reviews(self):
        """Test retrieving all reviews"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id)
        )

        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_update_review_valid(self):
        """Test updating a review's text"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        review_id = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id)
        ).get_json()["id"]

        response = self.client.put(
            f'/api/v1/reviews/{review_id}',
            json={"text": "Updated review"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["text"], "Updated review")

    def test_update_review_not_found(self):
        """Test updating a non-existent review"""
        response = self.client.put(
            '/api/v1/reviews/nonexistent-id',
            json={"text": "Update"}
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_review_valid(self):
        """Test deleting a valid review"""
        user_id = self.create_test_user()
        place_id = self.create_test_place(user_id)
        review_id = self.client.post(
            '/api/v1/reviews/',
            json=self.create_review_payload(user_id, place_id)
        ).get_json()["id"]

        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_review_not_found(self):
        """Test deleting a non-existent review"""
        response = self.client.delete('/api/v1/reviews/nonexistent-id')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
