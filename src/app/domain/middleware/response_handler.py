from flask import jsonify, make_response

class ResponseHandler:
    @staticmethod
    def success(data=None, message=None, status_code=200):
        response_data = {"status": "success"}

        if data is not None:
            response_data["data"] = data

        if message is not None:
            response_data["message"] = message

        response = make_response(jsonify(response_data), status_code)
        response.headers["Content-Type"] = "application/json"
        return response

    @staticmethod
    def error(message, status_code=400):

        return make_response(jsonify(message), status_code)