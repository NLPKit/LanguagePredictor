# -*- coding: utf-8 -*-

"""
This file contains the API server endpoints for serving language detection
requests
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import abort, jsonify, request

class PredictionEndpoint():
    """The endpoint for making predictions"""

    def __init__(self, model):
        self.model = model

    def predict(self, text):
        """Make a language prediction"""
        prediction = self.model.predict(text)
        language_code = prediction[0][0].replace("__label__", "")
        return language_code

    def endpoint(self):
        """The endpoint implementation"""
        req = request.get_json()
        text = ""
        try:
            text = req["text"]
        except KeyError:
            abort(400)

        return jsonify({
            "language": self.predict(text),
        })
