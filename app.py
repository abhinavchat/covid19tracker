from covid19tracker import create_app
from config import create_config
import os

app = create_app(create_config[os.getenv('ENVIRONMENT') or 'dev'])

if __name__ == "__main__":
    app.run()