# app.py
from flask import Flask, request, jsonify
from i200983 import add

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = add(num1, num2)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
