#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Language Detector is a RESTful web service for detecting the language of
arbitrary text.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import sys

import fastText
from flask import Flask, abort, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

class PredictionEndpoint():
    """The endpoint for making predictions"""

    def __init__(self, model):
        self.model = model

    def predict(self, text):
        """Make a language prediction"""
        prediction = self.model.predict(text)
        language = prediction[0][0].replace("__label__", "")
        confidence = prediction[1][0]
        return {
            "language": language,
            "confidence": confidence,
        }

    def endpoint(self):
        """The endpoint implementation"""
        req = request.get_json()
        text = ""
        try:
            text = req["text"]
        except KeyError:
            abort(400)

        return jsonify({
            "prediction": self.predict(text),
        })

def main():
    """The command entrypoint"""
    parser = argparse.ArgumentParser(prog="language_predictor")
    parser.add_argument(
        "--port",
        type=int,
        help="The port the API server should bind to ($PORT)",
        default=os.environ.get("PORT", 8080),
    )
    parser.add_argument(
        "--host",
        type=str,
        help="The local address the API server should bind to ($HOST)",
        default=os.environ.get("HOST", "127.0.0.1"),
    )
    parser.add_argument(
        "--model",
        type=str,
        help="[REQUIRED] The path to the fasttext model file ($MODEL)",
        default=os.environ.get("MODEL", None),
        required=True,
    )

    args = parser.parse_args(sys.argv[1:])

    model = fastText.load_model(args.model)
    app = Flask(__name__)
    predict = PredictionEndpoint(model)
    app.add_url_rule(
        "/api/v1/language/predict",
        "predict",
        view_func=predict.endpoint,
        methods=["POST"],
    )
    PrometheusMetrics(app)
    app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
