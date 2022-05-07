from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def running():
    return "Server is running"

@app.route("/project", methods=['POST'])
def project():
    req = request.get_json()
    project = req["action"]["detailParams"]["project"]["value"]
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": project
                    }
                }
            ]
        }
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)