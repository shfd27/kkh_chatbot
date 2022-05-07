from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def running():
    return "Server is running"

@app.route("/project",methods=['POST'])
def project():
    req = request.get_json()
    try:
        project = req["action"]["detailParams"]["project"]["value"]
        response = "프로젝트: "+project
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": response
                        }
                    }
                ]
            }
        }
    except:
        study = req["action"]["detailParams"]["study"]["value"]
        response = "스터디: "+study
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": response
                        }
                    }
                ]
            }
        }
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)