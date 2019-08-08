"""
* @author: Aditya Aman
* Helper Class for the application
"""
import os
import json
import uuid
from google.oauth2 import service_account
from . import Constants


class Helper:

    @staticmethod
    def get_data_from_json():
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir_path, 'data.json')
        return json.loads(open(json_path).read())

    @staticmethod
    def get_data_of_station(data, station):
        result = []
        for x in data['data']:
            if station in x:
                result.append(x)
        return result

    @staticmethod
    def get_data_for_month(data, station, month):
        station_data = Helper.get_data_of_station(data, station)
        for x in station_data:
            if month in x:
                return x
        return False

    @staticmethod
    def generate_unique():
        return str(uuid.uuid1())

    @staticmethod
    def get_credential():
        return service_account.Credentials.from_service_account_file(Constants.DIALOGFLOW_KEY)

    @staticmethod
    def get_intent(req):
        print(req['session'])
        return req.get("queryResult").get("action")

    @staticmethod
    def get_parameters(req):
        return req.get("queryResult").get("parameters")
