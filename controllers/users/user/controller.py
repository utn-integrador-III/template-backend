import json
from flask_restful import Resource, request
from flask import jsonify
from pymongo.common import RETRY_READS
from utils.responses import CodeResponses
from models.user.user import User as UserModel

class User(Resource):
    route = '/users'
        
    def get(self):
        data = UserModel.get_all()

        if len(data) < 1:
            return CodeResponses.customResponse({"message": "Couldn't found Users", "status": 200, "data":None}, None)

        return CodeResponses.successfullyResponse(None, data)

    # TODO: Field required validation
    def post(self):
       
        # Save to DB
        response = model.create_user()
        if type(response) is Exception:
            return CodeResponses.InternalServerErrorResponse(None, str(response))

        return CodeResponses.createdResponse(None, data)

