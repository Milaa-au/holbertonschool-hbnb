#!/usr/bin/python3

import unittest
import uuid
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def create_test_user(self):
        """Helper method to create a user for testing."""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": f"john{uuid.uuid4()}@example.com"
        })
        self.assertEqual(response.status_code, 201)
        return response.get_json()["id"]

    def test_create_place_valid(self):
        """Test creating a place with valid data."""

        owner_id = self.create_test_user()

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

        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Test Place")
        self.assertEqual(data["owner_id"], owner_id)

    def test_create_place_invalid(self):
        """Test creating a place with invalid data."""

        response = self.client.post('/api/v1/places/', json={
            "title": "Test Place",
            "description": "Nice place",
            "price": 100,
            "latitude": 45,
            "longitude": 3,
            "owner_id": "invalid-owner_id",
            "amenities": []
        })

        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertIn("error", data)

if __name__ == '__main__':
    unittest.main()
