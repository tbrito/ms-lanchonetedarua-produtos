from flask_restx import Api, Namespace, fields, Resource
from flask import jsonify
from app.domain.middleware.response_handler import ResponseHandler
from app.entrypoints.model.ping.ping_input import PingInput

api = PingInput.api

@api.route('/')
class PingNoParameters(Resource):
    
    def get(self):
        return ResponseHandler.success({"sucess": "pong"})