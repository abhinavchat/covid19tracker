import json
import requests
from config import Config

def get_data():
    return json.loads(requests.get(Config.BASE_URL).text)

def get_statewise_data():
    data = get_data()
    data = data.get("statewise")
    return data

def get_graph_data():
    data = get_data().get("cases_time_series")
    return {"labels": list(map(lambda k: k.get("date").strip(), data)), 
                   "confirmedCases": list(map(lambda k: int(k.get("totalconfirmed")), data)), 
                   "activeCases": list(map(lambda k: int(k.get("totalconfirmed")) - int(k.get("totaldeceased")) - int(k.get("totalrecovered")), data)), 
                   "deceasedCases": list(map(lambda k: int(k.get("totaldeceased")), data))}