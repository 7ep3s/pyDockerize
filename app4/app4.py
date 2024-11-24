from flask import Flask,json,jsonify,request

app = Flask(__name__)
app.debug = True

newInboxAvailable = False

@app.route("/")
def hello():
    return "App4 ^^"

@app.route("/InboxNotifier",methods=['POST'])
def inboxNotifier_event_post():
    global newInboxAvailable
    try:
        input = json.loads(request.data)
        newInboxAvailable = bool(input['newInboxAvailable'])
        print("updaing newInboxAvailable: " + str(newInboxAvailable))
        return jsonify("success"),200
    except:
        return jsonify("invalid request"),400
    
@app.route("/InboxNotifier",methods=['GET'])
def inboxNotifier_event_get():
    global newInboxAvailable
    try:
        return jsonify(newInboxAvailable),200
    except:
        return jsonify("invalid request"),400

if __name__ == '__main__':
   app.run(port=50001)