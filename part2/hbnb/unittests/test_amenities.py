#!/usr/bin/python3

import unittest
from app import create_app
from app.services import facade


class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

        # Clear storage
        facade.amenity_repo.storage = {}

    def create_amenity_payload(self, name="WiFi"):
        return {
            "name": name
        }

    def test_create_amenity_valid(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json=self.create_amenity_payload()
        )

        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "WiFi")

    def test_create_amenity_invalid_empty_name(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json=self.create_amenity_payload(name="")
        )

        self.assertEqual(response.status_code, 400)

    def test_create_amenity_invalid_no_data(self):
        response = self.client.post('/api/v1/amenities/')
        self.assertEqual(response.status_code, 400)

    def test_get_all_amenities(self):
        self.client.post(
            '/api/v1/amenities/',
            json=self.create_amenity_payload()
        )

        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_get_amenity_by_id_valid(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json=self.create_amenity_payload()
        )
        amenity_id = response.get_json()["id"]

        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["id"], amenity_id)

    def test_get_amenity_not_found(self):
        response = self.client.get('/api/v1/amenities/nonexistent-id')
        self.assertEqual(response.status_code, 404)

    def test_update_amenity_valid(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json=self.create_amenity_payload()
        )
        amenity_id = response.get_json()["id"]

        response = self.client.put(
            f'/api/v1/amenities/{amenity_id}',
            json={"name": "Updated WiFi"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Updated WiFi")

    def test_update_amenity_not_found(self):
        response = self.client.put(
            '/api/v1/amenities/nonexistent-id',
            json={"name": "Updated"}
        )
        self.assertEqual(response.status_code, 404)

    def test_update_amenity_invalid_data(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json=self.create_amenity_payload()
        )
        amenity_id = response.get_json()["id"]

        response = self.client.put(
            f'/api/v1/amenities/{amenity_id}',
            json={}
        )

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
