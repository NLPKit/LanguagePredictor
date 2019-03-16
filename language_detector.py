"""
Language Detector is a RESTful web service for detecting the language of
arbitrary text.
"""

import argparse
import sys

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

import api.server

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

    parser_train = subparsers.add_parser(
        "train",
        help="Train a language detection model",
    )
    parser_train.add_argument(
        "--iterations",
        type=int,
        help="The number of iterations",
        default=9001,
    )

    args = parser.parse_args(sys.argv[1:])
    if args.mode == "run":
        app = Flask(__name__)
        app.add_url_rule(
            "/api/v1/language/predict",
            "predict",
            view_func=api.server.predict,
            methods=["POST"],
        )
        PrometheusMetrics(app)
        app.run(host=args.host, port=args.port)
    elif args.mode == "train":
        print("Training is not implemented yet...")

if __name__ == "__main__":
    main()
