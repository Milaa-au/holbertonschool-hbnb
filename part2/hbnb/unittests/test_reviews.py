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

    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        api = Api(app)
        api.add_namespace(reviews_api, path='/api/v1/reviews')
        @app.route('/health')
        def health_check():
            return "OK", 200
        app.config['TESTING'] = True
        cls.client = app.test_client()

    @patch.object(facade, 'create_review')
    def test_create_review(self, mock_create_review):
        mock_review = MagicMock()
        mock_review.id = "123"
        mock_review.text = "Great place!"
        mock_review.rating = 5
        mock_review.user.id = "user_123"
        mock_review.place.id = "place_123"
        mock_create_review.return_value = mock_review
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "rating": 5,
            "user_id": "user_123",
            "place_id": "place_123"
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            "id": "123",
            "text": "Great place!",
            "rating": 5,
            "user_id": "user_123",
            "place_id": "place_123"
        })

    @patch.object(facade, 'get_all_reviews')
    def test_get_all_reviews(self, mock_get_all_reviews):
        mock_reviews = [
            MagicMock(id="123", text="Great place!", rating=5, user=MagicMock(
                id="user_123"), place=MagicMock(id="place_123")),
            MagicMock(id="124", text="Not bad", rating=3, user=MagicMock(
                id="user_124"), place=MagicMock(id="place_123"))
        ]
        mock_get_all_reviews.return_value = mock_reviews

        response = self.client.get('/api/v1/reviews/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]["text"], "Great place!")
        self.assertEqual(response.json[1]["rating"], 3)

    @patch.object(facade, 'get_review')
    def test_get_review_by_id(self, mock_get_review):
        mock_review = MagicMock(id="123", text="Great place!", rating=5, user=MagicMock(
            id="user_123"), place=MagicMock(id="place_123"))
        mock_get_review.return_value = mock_review

        response = self.client.get('/api/v1/reviews/123')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["id"], "123")
        self.assertEqual(response.json["text"], "Great place!")

    @patch.object(facade, 'update_review')
    def test_update_review(self, mock_update_review):
        mock_review = MagicMock(id="123", text="Updated review", rating=4, user=MagicMock(
            id="user_123"), place=MagicMock(id="place_123"))
        mock_update_review.return_value = mock_review

        response = self.client.put('/api/v1/reviews/123', json={
            "text": "Updated review",
            "rating": 4,
            "user_id": "user_123",
            "place_id": "place_123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["text"], "Updated review")
        self.assertEqual(response.json["rating"], 4)

    @patch.object(facade, 'delete_review')
    def test_delete_review(self, mock_delete_review):
        mock_delete_review.return_value = True

        response = self.client.delete('/api/v1/reviews/123')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {"message": "Review deleted successfully"})

    @patch.object(facade, 'get_reviews_by_place')
    def test_get_reviews_for_place(self, mock_get_reviews_by_place):
        mock_reviews = [
            MagicMock(id="123", text="Great place!", rating=5, user=MagicMock(
                id="user_123"), place=MagicMock(id="place_123")),
            MagicMock(id="124", text="Not bad", rating=3, user=MagicMock(
                id="user_124"), place=MagicMock(id="place_123"))
        ]
        mock_get_reviews_by_place.return_value = mock_reviews

        response = self.client.get('/api/v1/reviews/places/place_123/reviews')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]["text"], "Great place!")
        self.assertEqual(response.json[1]["rating"], 3)


if __name__ == "__main__":
    unittest.main()
