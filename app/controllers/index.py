"""
* @author: Aditya Aman (aditya.aman@keito.works)
"""
from flask import (
    Blueprint, request, render_template,
    make_response, jsonify, session
)
from .helper import Helper
import dialogflow
from . import Constants


bp = Blueprint('index', __name__, url_prefix="/")
SESSION_ID = "session_id"


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    session[SESSION_ID] = Helper.generate_unique()
    return render_template('index/index.html')


@bp.route('/send_message', methods=["POST"])
def send_message():
    message = request.form['message']
    res = detect_intent(message, session[SESSION_ID])
    return jsonify({"message": res})


@bp.route("/web_hook", methods=["POST"])
def web_hook():
    req = request.get_json(silent=True)
    return make_response(jsonify({"fulfillmentText": f"ok google.{Helper.get_intent(req)}"}))


def detect_intent(text, session_id):
    session_client = dialogflow.SessionsClient(
        credentials=Helper.get_credential()
    )
    ss = session_client.session_path(
        Constants.PROJECT_ID, session_id
    )
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code="en")
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=ss, query_input=query_input)
        return response.query_result.fulfillment_text
