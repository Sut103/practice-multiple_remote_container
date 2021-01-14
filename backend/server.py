from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def index():
    response = {
        "message": "Hello from Flask Container"
    }

    return make_response(jsonify(response))


if __name__ == "__main__":
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'prod')
    app.debug = ENVIRONMENT == 'dev'
    app.run(host='0.0.0.0', port=5000)
