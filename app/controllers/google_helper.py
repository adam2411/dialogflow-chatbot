"""
* @author: Aditya Aman
* Google Helper to help with dialogflow
"""

google = {
    "expectUserResponse": True,
    "richResponse": {
        "items": [
            {
                "simpleResponse": {
                    "textToSpeech": ""
                }
            }
        ],
        "suggestions": []
    }
}
context = {
    "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
    "lifespanCount": 1,
    "parameters": ""
}


def get_google_payload(resp, suggestions=[], user_response=True):
    google['expectUserResponse'] = user_response
    rp = google["richResponse"]
    rp['items'][0]["simpleResponse"]["textToSpeech"] = resp
    rp["suggestions"] = suggestions
    google['richResponse'] = rp
    return google


def set_context(req, context_name, params={}, ls=1):
    name = req['session'] + f"/contexts/{context_name}"
    context["name"] = name
    context["parameters"] = params
    context["lifespanCount"] = ls
    return context


