from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def index():
    response = {
        "message": "Hello from Flask Container"
    }

    return make_response(jsonify(response))


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
