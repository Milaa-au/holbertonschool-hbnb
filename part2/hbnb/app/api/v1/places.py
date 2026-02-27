review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):

        """
        Retrieve all reviews associated with a specific location.

        This method first checks whether the location exists using its
        identifier, then returns the list of reviews linked to
        that location using the facade layer.

        Args:
            place_id (str): Unique identifier for the location.

        Returns:
        tuple:
            - list: List of reviews associated with the place.
            - int: HTTP code 200 if successful.

        If the place does not exist:
            - dict: Error message.
            - int: HTTP code 404.
        """

        place = facade.get_place(place_id)

        if not place:
            return {"message": "Place not found"}, 404
        reviews = facade.get_reviews_by_place(place_id)

        return [r.to_dict() for r in reviews], 200