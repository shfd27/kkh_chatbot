from flask import Flask, request, jsonify
from notion_py import registration, attend


app = Flask(__name__)

@app.route("/")
def running():
    return "Server is running"

@app.route("/project",methods=['POST'])
def project():
    req = request.get_json()
    print(req)
    if req["intent"]["name"] == "project":
        project = req["action"]["detailParams"]["project"]["value"]
        response = "프로젝트: "+project
        return jsonify(send(response))
    if req["intent"]["name"] == "study":
        study = req["action"]["detailParams"]["study"]["value"]
        response = "스터디: "+study
        return jsonify(send(response))
    if req["intent"]["name"] == "command":
        print(req["action"]["params"])
        if req["userRequest"]["utterance"].startswith("/"):
            if "등록" == req["action"]["params"]["command"]:
                try:
                    project = req["action"]["params"]["study"]
                except:
                    project = req["action"]["params"]["project"]
                state = registration.make_page(project)
                print("state:", state)
                return jsonify(send(project))    # response does not send because of notion processing time
            if "출석" == req["action"]["params"]["command"]:
                try:
                    project = req["action"]["params"]["study"]
                except:
                    project = req["action"]["params"]["project"]
                name = req["userRequest"]["utterance"].split(" ")[-1]
                state = attend.attend(project, name)
                print("state:", state)
                return jsonify(send(project))    # response does not send because of notion processing time

def send(res):
    return {
            "version": "2.0",
            "template": {"outputs": [{"simpleText": {"text": res}}]}
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)