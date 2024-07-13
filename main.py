from flask import *
from utils.detect_sql_injection import detect_sql_injection

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Sai chandran's Assessment."


@app.route("/v1/sanitized/input/", methods=["POST"])
def sanitize_input():
    if not request.is_json:
        return jsonify({"Error": "Invalid Input, Please provide the data in JSON format."}), 400

    data = request.get_json()

    if 'input' not in data:
        return jsonify({"Error": "No input given."}), 400

    input_value = data.get('input', '')
    if (detect_sql_injection(input_value)):
        return jsonify({"result": "unsanitized"})
    else:
        return jsonify({"result": "sanitized"})


if __name__ == "__main__":
    app.run(debug=True)
