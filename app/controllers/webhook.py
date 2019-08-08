from flask import Blueprint, request, make_response, jsonify, session
from .helper import Helper
from . import google_helper


SESSION_ID = "session_id"
bp = Blueprint('webhook', __name__, url_prefix="/gl")


@bp.route('/web_hook', methods=["POST"])
def web_hook():
    req = request.get_json(silent=True)
    ft, google, context = handle_intent(req)
    if not context:
        context = []
    return make_response(jsonify(
        {
            "fulfillmentText": ft,
            "payload": {
                "google": google
            },
            "outputContexts": context
        }
    ))


def handle_intent(req):
    intent = Helper.get_intent(req)
    print(intent)
    if intent == "intent_register":
        msg = "Okay, Let's start by getting your Name."
        return msg, google_helper.get_google_payload(msg), []
    elif intent == "intent_name":
        return handle_name(req)
    elif intent == "intent_last_name":
        return handle_last_name(req)
    elif intent == "intent_gender":
        return handle_gender(req)
    elif intent == "intent_dob":
        return handle_dob(req)
    elif intent == "intent_dob_year":
        return handle_dob_year(req)


def handle_name(req):
    param = Helper.get_parameters(req)
    if param['lname'] == "" or param['fname'] == param['lname']:
        context = list()
        context.append(google_helper.set_context(req, "last_name", ls=5))
        msg = "What is your last name?"
        google = google_helper.get_google_payload(msg)
        return msg, google, context
    return ask_gender()


def handle_last_name(req):
    param = Helper.get_parameters(req)
    return ask_gender()


def ask_gender():
    msg = "What is your gender?"
    suggestion = [
        {"title": "Male"},
        {"title": "Female"}
    ]
    google = google_helper.get_google_payload(msg, suggestion)
    return msg, google, None


def handle_gender(req):
    msg = "What is your date of birth?"
    google = google_helper.get_google_payload(msg)
    return msg, google, None


def handle_dob(req):
    param = Helper.get_parameters(req)
    print(req)
    if 'UUUU' in param['date']:
        context = list()
        context.append(google_helper.set_context(req, "get_dob_year"))
        msg = "What is your birth year?"
        google = google_helper.get_google_payload(msg)
        return msg, google, context
    return finish_register(req)


def handle_dob_year(req):
    print(req)
    param = Helper.get_parameters(req)
    return finish_register(req)


def finish_register(req):
    oc = req['queryResult']["outputContexts"]
    proceed = None
    for o in oc:
        if "fname" in o['parameters']:
            year = o['parameters']['date'];
            if 'UUUU' in year:
                x = o['parameters']['date'].split('-')
                year = str(int(o['parameters']['date-period'])) + f"-{x[1]}-{x[2]}"
            proceed = {
                "fname": o['parameters']['fname'],
                "lname": o['parameters']['lname'],
                "gender": o['parameters']['sex'],
                "year": year
            }
    msg = f"Your name is {proceed['fname']} {proceed['lname']} and you are a {proceed['gender']} born on {proceed['year']}"
    google = google_helper.get_google_payload(msg, user_response=False)
    return msg, google, None

