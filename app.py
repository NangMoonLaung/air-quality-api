from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.json
    print(data)
    return jsonify({"status":"received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)