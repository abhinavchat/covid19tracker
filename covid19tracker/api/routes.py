from covid19tracker.api import api
from flask import jsonify
from config import Config
import requests, json

def get_data():
    return json.loads(requests.get(Config.BASE_URL).text)


@api.route('/')
def index():
    return jsonify(get_data())

@api.route('/statewise', methods=['GET'])
def get_statewise():
    data = get_data()
    data = data.get("statewise")
    data = [obj for obj in data if obj.get("statecode") != "TT"]
    return jsonify(data)

@api.route('/graph', methods=['GET'])
def get_confirmed():
    data = get_data().get("cases_time_series")
    print(list(map(lambda k: k.get("date").strip(), data)))
    sample_data = {"labels": list(map(lambda k: k.get("date").strip(), data)), 
                   "confirmedCases": list(map(lambda k: int(k.get("totalconfirmed")), data)), 
                   "activeCases": list(map(lambda k: int(k.get("totalconfirmed")) - int(k.get("totaldeceased")) - int(k.get("totalrecovered")), data)), 
                   "deceasedCases": list(map(lambda k: int(k.get("totaldeceased")), data))}
    return jsonify(sample_data)
