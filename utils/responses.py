from flask import Response
import json


class CodeResponses:
    @classmethod
    def customResponse(self, response, exception):
        return Response(
            json.dumps(
                {"msg": {
                    "status": response["status"],
                    "message": response["message"],
                    "exception": exception
                },
                "data": response["data"],

                }),
            mimetype='application/json', status=int(response["status"]))

    @classmethod
    def statusOnline(self, exception):
        response = {"status": 200, "message": "status online", 'data':None}
        return self.customResponse(response, exception)

    @classmethod
    def successfullyResponse(self, exception, data):
        response = {"status": 200, "message": "Ok", "data": data}
        return self.customResponse(response, exception)

    @classmethod
    def createdResponse(self, exception, data):
        response = {"status": 201, "message": "Created Successfully", 'data': data}
        return self.customResponse(response, exception)
    
    @classmethod
    def alreadyExist(self, exception):
        response = {"status": 403, "message": "This already exist", 'data':None}
        return self.customResponse(response, exception)

    @classmethod
    def deletedResponse(self, exception):
        response = {"status": 200, "message": "Deleted Successfully",  "data":None}
        return self.customResponse(response, exception)

    @classmethod
    def updatedResponse(self, exception, data):
        response = {"status": 200, "message": "Updated Successfully", 'data': data}
        return self.customResponse(response, exception)
    
    @classmethod
    def noUpdatedResponse(self, exception, ):
        response = {"status": 404, "message": "No info to Update", 'data': None}
        return self.customResponse(response, exception)

    @classmethod
    def retrievedResponse(self, exception):
        response = {"status": 200, "message": "Retrieved Successfully"}
        return self.customResponse(response, exception)

    @classmethod
    def missingInfoResponse(self, exception):
        response = {"status": 422, "message": "Missing Information", 'data': None}
        return self.customResponse(response, exception)

    @classmethod
    def QuestionsNotFoundResponse(self, exception):
        response = {"status": 404, "message": "Not Found For This Owner"}
        return self.customResponse(response, exception)

    @classmethod
    def QuestionNotFoundResponse(self, exception):
        response = {"status": 404, "message": "Not Found For This Id", "data": None}
        return self.customResponse(response, exception)

    @classmethod
    def noResultsFound(self, exception):
        response = {"status": 423, "message": "No Results Found", "data": None}
        return self.customResponse(response, exception)

    @classmethod
    def InternalServerErrorResponse(self, exception):
        response = {"status": 500, "message": "Internal Server Error"}
        return self.customResponse(response, exception)

