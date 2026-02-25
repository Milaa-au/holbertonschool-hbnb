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
        """Register a new amenity"""
        data = request.get_json()

        if not data:
            return {"message": "Invalid input data"}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        try:
            amenity = get_amenity(amenity_id)
        except ValueError:
            return {"message": "Amenity not found"}, 404

        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = request.get_json()

        if not data:
            return {"message": "Invalid input data"}, 400

        try:
            updated_amenity = update_amenity(amenity_id, data)
        except ValueError:
            return {"message": "Amenity not found"}, 404

        return updated_amenity.to_dict(), 200