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
        try:
            data = request.json
            review_obj = facade.create_review(data)
            return {
                "Review id": str(review_obj.id),
                "text": review_obj.text,
                "rating": int(review_obj.rating),
                "user_id": str(review_obj.user.id),
                "place_id": str(review_obj.place.id)
            }, 201
        except Exception as e:
            return {'message': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        reviews = facade.get_all_reviews()
        return [
            {
                "Review id": str(r.id),
                "text": r.text,
                "rating": int(r.rating),
                "user_id": str(r.user.id),
                "place_id": str(r.place.id)
            }
            for r in reviews
        ], 200

@api.route('/<review_id>')
class ReviewResource(Resource):

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
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
        delete_review = facade.get_review(review_id)
        if not delete_review:
            return {'error': 'Review not found'}, 404

        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)

        if not place:
            return {"message": "Place not found"}, 404
        reviews = facade.get_reviews_by_place(place_id)

        return [r.to_dict() for r in reviews], 200

