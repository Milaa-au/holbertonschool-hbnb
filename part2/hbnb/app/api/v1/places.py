"""
User API namespace.

This module defines REST endpoints for managing places, including
creation, retrieval, and update operations. It relies on a facade
service layer to handle business logic and data persistence.
"""


from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(
        required=True,
        description='Latitude of the place'
    ),
    'longitude': fields.Float(
        required=True,
        description='Longitude of the place'
    ),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(
        fields.String, required=True,
        description="List of amenities ID's"
    )
})

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

@api.route('/')
class PlaceList(Resource):
    """
    Resource for operations on the place collection.

    Provides endpoints to create a new place and to retrieve
    the list of all places.
    """
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new place.

        Retrieves the JSON payload from the API request and attempts to create
        a new place using the facade. If creation fails due to invalid data,
        returns a 400 response with an error message.

        Returns:
        tuple: A JSON dictionary containing the new place details and
        the HTTP status code 201 if successful, or an error message and
        status code 400 if creation fails.
        """
        place_data = api.payload

        try:
            new_place = facade.create_place(place_data)
        except ValueError as error:
            return {'error': str(error)}, 400
        return {
            'id': new_place.id,
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner.id
        }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """
        Retrieve the list of all locations.

        Retrieves all locations via the facade and returns a simplified list
        containing the ID, title, latitude, and longitude of each location.

        Returns:
        tuple: A list of dictionaries representing each location and
        the HTTP 200 code.
        """
        places = facade.get_all_places()
        List_places = []
        for place in places:
            List_places.append({
                'id': place.id,
                'title': place.title,
                'latitude': place.latitude,
                'longitude': place.longitude
            })
        return List_places, 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Retrieve details of a place by its ID.

        Retrieves a specific place via its ID. If the place does not exist,
        returns a 404 error with an appropriate message.

        Args:
        place_id (str): The unique identifier of the place to retrieve.

        Returns:
        tuple: A dictionary containing detailed information
        about the place and HTTP code 200 if found, or an error message
        with code 404 if not found."""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [
                {
                    'id': amenity.id,
                    'name': amenity.name
                }
                for amenity in place.amenities
            ]
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """
        Update place information.

        Accepts JSON data from the request and attempts to update
        an existing place identified by place_id. If the data is invalid,
        returns a 400 response. If the place does not exist, returns a 404 response.

        Args:
        place_id (str): The unique identifier of the place to update.

        Returns:
        tuple: A dictionary containing the updated information
        for the place and HTTP code 200 if successful, or an error message
        with code 400 or 404 if unsuccessful.
        """
        place_data = api.payload

        try:
            update_place = facade.update_place(place_id, place_data)
        except ValueError as error:
            return {'error': str(error)}, 400

        if not update_place:
            return {'error': 'Place not found'}, 404

        return {
            'id': update_place.id,
            'title': update_place.title,
            'description': update_place.description,
            'price': update_place.price,
            'latitude': update_place.latitude,
            'longitude': update_place.longitude,
            'owner_id': update_place.owner.id
        }, 200

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

