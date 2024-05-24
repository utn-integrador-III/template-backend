import json
from flask_restful import Resource, request
from flask import jsonify
from pymongo.common import RETRY_READS
from utils.responses import CodeResponses
from models.book.book import Book as BookModel
# from .parser import query_parser

class Book(Resource):
    route = '/books/'
        
    def get(self):
        if 'title' in request.args:
            data = BookModel.get_by_name(request.args['title'])
        elif 'book_key' in request.args:
            data = BookModel.get_book_by_key(request.args['book_key'])
        if len(data) < 1:
            return CodeResponses.customResponse({"message": "Couldn't found Users", "status": 200, "data":None}, None)
            
        return CodeResponses.successfullyResponse(None, data)

    # TODO: Field required validation
    def post(self):
        # TODO: Add validations
        data = request.get_json()

        # Create a new deal
        new_user = UserModel(**data)

        # Perform validations

        # Save to DB
        response = new_user.create_user()
        if type(response) is Exception:
            return CodeResponses.InternalServerErrorResponse(None, str(response))

        return CodeResponses.createdResponse(None, data)

