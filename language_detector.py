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
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from api.server import PredictionEndpoint

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
