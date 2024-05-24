from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from service import addServiceLayer
from decouple import config

app = Flask(__name__)
app.debug = config('FLASK_DEBUG', cast=bool)
api = Api(app)

if config('BOOKING_API_ENVIRONMENT')=='Development':
    cors = CORS(app, resources={r"/api/openapi": {"origins": "*"}, r"/*": {"origins": "*"}})
    
addServiceLayer(api)

if __name__ == '__main__':
    app.run(host=config('FLASK_RUN_HOST'), port=config('API_PORT'))


