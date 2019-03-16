"""This file contains the API server for serving language detection requests"""

from flask import Flask, jsonify

class Server:
    """Server is the class that implements the API server"""
    def __init__(self, name, host, port):
        self.host = host
        self.port = port

        self.app = Flask(name)
        self.app.add_url_rule("/", "index", view_func=self.index)

    def run(self):
        """start the server"""
        self.app.run(host=self.host, port=self.port)

    def index(self):
        """The base URL on the server"""
        return jsonify({"port": self.port})
