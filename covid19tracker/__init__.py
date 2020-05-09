from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    cors = CORS(app)

    from covid19tracker.api import api
    app.register_blueprint(api)

    return app