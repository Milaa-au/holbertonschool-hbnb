from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):

    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):

        """
        Create a new review.

        This endpoint receives JSON data from the request payload
        and creates a new review using the facade layer.

        Returns:
            tuple:
            - dict: The created review data (id, rating, text,
              place_id, user_id).
            - int: HTTP status code 201 if creation succeeds.

        If the input data is invalid:
            - dict: Error message.
            - int: HTTP status code 400.
        """

        data = api.payload
        new_review = facade.create_review(data)

        if not new_review:
            return {'error': 'Invalid input data'}, 400

        return {'id': new_review.id,
                'rating': new_review.rating,
                'text': new_review.text,
                'place_id': new_review.place_id,
                'user_id': new_review.user_id}, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):

        """Retrieve the list of all reviews.

        This method queries the facade layer to obtain
        all reviews stored in the system.

        Returns:
            tuple:
            - dict: Review data.
            - int: HTTP code 200 if successful.
        """

        reviews = facade.get_all_reviews()

        return {'id': new_review.id,
                'rating': new_review.rating,
                'text': new_review.text,
                'place_id': new_review.place_id,
                'user_id': new_review.user_id}, 200

@api.route('/<review_id>')
class ReviewResource(Resource):

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):

        """Retrieve the details of a review by its ID.

        This method searches for a review based on its ID
        via the facade layer.

        Args:
        review_id (str): Unique identifier of the review.

        Returns:
        tuple:
            - dict: The review data, if it exists.
            - int: HTTP code 200 if successful.

        If the review does not exist:
            - dict: Error message.
            - int: HTTP code 404.

        Translated with DeepL.com (free version)
        """

        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        return {'id': new_review.id,
                'rating': new_review.rating,
                'text': new_review.text,
                'place_id': new_review.place_id,
                'user_id': new_review.user_id}, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):

        """
        Update review information.

        This method updates an existing review based on
        the JSON data received in the request.

        Args:
            review_id (str): Unique identifier for the review.

        Returns:
        tuple:
            - dict: Updated review data.
            - int: HTTP code 200 if successful.

        If the review does not exist:
            - dict: Error message.
            - int: HTTP code 404.

        If the data is invalid:
            - dict: Error message.
            - int: HTTP code 400.
        """

        data = api.payload
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        updated_review = facade.update_review(review_id, data)

        if not updated_review:
            return {'error': 'Invalid input data'}, 400

        return {'id': new_review.id,
                'rating': new_review.rating,
                'text': new_review.text,
                'place_id': new_review.place_id,
                'user_id': new_review.user_id}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')

    def delete(self, review_id):

        """Delete a review.

        This method deletes an existing review via its
        identifier using the facade layer.

        Args:
        review_id (str): Unique identifier of the review.

        Returns:
        tuple:
            - dict: Confirmation message.
            - int: HTTP code 200 if successful.

        If the review does not exist:
            - dict: Error message.
            - int: HTTP code
        """

        delete_review = facade.delete_review(review_id)

        if not delete_review:
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200
