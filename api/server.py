"""
This file contains the API server endpoints for serving language detection
requests
"""

from flask import abort, jsonify, request

class PredictionEndpoint():
    """The endpoint for making predictions"""

    def __init__(self, model):
        self.model = model

    def predict(self, text):
        """Make a language prediction"""
        return self.model.predict(text)

    def endpoint(self):
        """The endpoint implementation"""
        req = request.get_json()
        text = ""
        try:
            text = req["text"]
        except KeyError:
            abort(400)

        prediction = self.predict(text)
        language = prediction[0][0].replace("__label__", "")

        return jsonify({
            "language": language,
        })
