import urllib.request
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/carrier-look/<phone_num>")
def carrier_look(phone_num):
    try:
        with urllib.request.urlopen('http://apilayer.net/api/validate?access_key=00b3b3913564761de02ac0d48377f156&number='+phone_num) as response:
            data = json.loads(response.read().decode('utf-8'))
            if not data['valid']:
                return jsonify({"error": "Invalid phone number"}), 404
            else:
                return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
