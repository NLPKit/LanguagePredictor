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

def main():
    """The command entrypoint"""
    parser = argparse.ArgumentParser(prog="language_detector")
    subparsers = parser.add_subparsers(dest="mode")

    parser_run = subparsers.add_parser("run", help="Run the API server")
    parser_run.add_argument(
        "--port",
        type=int,
        help="The port of the API server",
        default=8080,
    )
    parser_run.add_argument(
        "--host",
        type=str,
        help="The host of the API server",
        default="127.0.0.1",
    )
    parser_run.add_argument(
        "--model",
        type=str,
        help="The fasttext model file",
        required=True,
    )

    args = parser.parse_args(sys.argv[1:])

    if args.mode == "run":
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

    else:
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
