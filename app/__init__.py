"""
* @author: Aditya Aman (aditya.aman@keito.works)
* This is a basic flask application that builds a chat-bot
* using dialogflow.
"""
from flask import Flask
from .controllers import index, webhook


def create_app():
    app = Flask(__name__)
    app.secret_key = "safjkdbsafb8123123"
    app.register_blueprint(index.bp)
    app.register_blueprint(webhook.bp)
    return app
