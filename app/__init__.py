"""
* @author: Aditya Aman (aditya.aman@keito.works)
* This is a basic flask application that builds a chat-bot
* using dialogflow.
"""
from flask import Flask
from .controllers import index


def create_app():
    app = Flask(__name__)
    app.register_blueprint(index.bp)
    return app
