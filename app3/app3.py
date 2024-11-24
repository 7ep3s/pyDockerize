from flask import Flask,json,jsonify,request

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "App3 ^^"

@app.route("/doStuff",methods = ['POST'])
def do_stuff():
    #try:
    asd = json.loads(request.data)
    print(asd)
    return asd,200
    #except:
    #   return jsonify("invalid request"),400

if __name__ == '__main__':
   app.run(port=50000)