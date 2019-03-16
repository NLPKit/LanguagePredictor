"""
This file contains the API server endpoints for serving language detection
requests
"""

from flask import abort, jsonify, request

def predict():
    """The endpoint for making predictions"""
    req = request.get_json()
    text = ""
    try:
        text = req["text"]
    except KeyError:
        abort(400)

    return jsonify({
        "text": text,
    })
