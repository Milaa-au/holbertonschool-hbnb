#!/usr/bin/python3

import unittest
from app import create_app
from app.services import facade


class TestAmenityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(amenities_api, path='/api/v1/amenities')
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post(
            '/api/v1/amenities/', json={'name': 'Pool'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], 'Pool')

    def test_get_all_amenities(self):
        facade.create_amenity({'name': 'WiFi'})
        facade.create_amenity({'name': 'Cafe'})
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) >= 2)

    def test_get_amenity_by_id(self):
        amenity = facade.create_amenity({'name': 'Yoga'})
        response = self.client.get(f'/api/v1/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Yoga')

    def test_update_amenity(self):
        amenity = facade.create_amenity({'name': 'cleaning'})
        response = self.client.put(
            f'/api/v1/amenities/{amenity.id}', json={'name': 'cleaning lady'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'cleaning lady')


if __name__ == "__main__":
    unittest.main()
