"""This file contains the API server for serving language detection requests"""

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

class Server:
    """Server is the class that implements the API server"""
    def __init__(self, name, host, port):
        self.host = host
        self.port = port

        self.app = Flask(name)
        self.app.add_url_rule("/api/v1/language/predict", "predict", view_func=self.predict)

        self.metrics = PrometheusMetrics(self.app)

    def run(self):
        """start the server"""
        self.app.run(host=self.host, port=self.port)

    def predict(self):
        """The endpoint for making predictions"""
        return jsonify({"port": self.port})
