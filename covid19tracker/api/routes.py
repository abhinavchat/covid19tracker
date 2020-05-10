from covid19tracker.api import api
from flask import jsonify
from covid19tracker.api.services import *

@api.route('/')
def index():
    return jsonify(get_data())

@api.route('/statewise', methods=['GET'])
def get_statewise():
    return jsonify(get_statewise_data())

@api.route('/graph', methods=['GET'])
def get_confirmed():
    return jsonify(get_graph_data())
