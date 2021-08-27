from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to the flask tutorials"

@app.route('/calculate', methods=['POST'])
def predict_calculate():

    data = request.get_json(force=True)
    #print(data)
    sum = data["a"] + data["b"]
    return json.dumps({"sum":sum})

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8080, debug = True)
