from flask import Flask
from flask_cors import CORS

def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    cors = CORS(app)

    from covid19tracker.api import api
    app.register_blueprint(api)

    return app