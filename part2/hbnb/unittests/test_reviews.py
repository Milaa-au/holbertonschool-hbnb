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
def test_review_init(self):
        review = Review("Great place!", 5, "user_id_123", "place_id_456")
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.user_id, "user_id_123")
        self.assertEqual(review.place_id, "place_id_456")

    def test_text_validation(self):
        with self.assertRaises(ValueError):
            Review("", 5, "user_id_123", "place_id_456")

        with self.assertRaises(ValueError):
            Review("A" * 501, 5, "user_id_123", "place_id_456")

    def test_rating_validation(self):
        with self.assertRaises(ValueError):
            Review("Great place!", 0, "user_id_123", "place_id_456")

        with self.assertRaises(ValueError):
            Review("Great place!", 6, "user_id_123", "place_id_456")


class TestAmenityModel(unittest.TestCase):
    def test_amenity_init(self):
        amenity = Amenity("WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Amenity("")

        with self.assertRaises(ValueError):
            Amenity("A" * 51)

if __name__ == "__main__":
    unittest.main()
