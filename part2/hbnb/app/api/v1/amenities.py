#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):

        """
        Create a new amenity.

        This method retrieves the JSON data sent in the
        request and calls the facade layer to create a
        new amenity.

        Returns:
        tuple:
            - dict: Data for the created amenity (id, name).
            - int: HTTP code 201 if successful.

        If the data is invalid:
            - dict: Error message.
            - int: HTTP code 400.
        """

        amenity_data = api.payload
        amenity_new = facade.create_amenity(amenity_data)
        if not new_amenity:
            return {'error': 'Invalid input data'}, 400
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):

        """
        Retrieve the list of all amenities.

        This method queries the facade layer to
        retrieve all registered amenities.

        Returns:
        tuple:
            - list: List of amenities in dictionary format.
            - int: HTTP code 200 if successful.
        """

        amenities = get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):

        """
        Retrieve the details of an amenity by its ID.

        This method searches for a specific amenity
        using its ID via the facade layer.

        Args:
        amenity_id (str): Unique ID of the amenity.

        Returns:
        tuple:
            - dict: The amenity data if it exists.
            - int: HTTP code 200 if successful.

        If the amenity does not exist:
            - dict: Error message.
            - int: HTTP code 404.
        """

        try:
            amenity = get_amenity(amenity_id)
        except ValueError:
            return {"error": "Amenity not found"}, 404

        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):

        """
        Update amenity information.

        This method updates an existing amenity
        based on the JSON data received in the request.

        Args:
        amenity_id (str): Unique identifier for the amenity.

        Returns:
        tuple:
            - dict: Updated amenity data.
            - int: HTTP code 200 if successful.

        If the amenity does not exist:
            - dict: Error message.
            - int: HTTP code 404.

        If the data is invalid:
            - dict: Error message.
            - int: HTTP code 400.
        """

        data = request.get_json()

        if not data:
            return {"error": "Invalid input data"}, 400

        try:
            updated_amenity = update_amenity(amenity_id, data)
        except ValueError:
            return {"error": "Amenity not found"}, 404

        return updated_amenity.to_dict(), 200
