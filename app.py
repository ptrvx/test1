from flask import Flask
from flask import request, make_response, redirect
import json

app = Flask(__name__)

@app.route('/')
def Main():
    return 'Welcome to the Updated Test API'

@app.route('/test', methods=['GET'])
def GetAll():
    if request.method == "GET":
        result = json.dumps(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        return result

@app.route('/api', methods=['GET', 'POST', 'PUT'])
def Add():
    nums = request.args
    num1 = int(nums['prvi'])
    num2 = int(nums['drugi'])
    op = nums['op']
    result = num1 + num2
    if op == 'minus':
        result = num1 - num2
    return json.dumps({'result': result})

@app.route('/json', methods=['POST'])
def AddJson():
    if request.method == 'POST':
        nums = request.get_json()
        num1 = int(nums['prvi'])
        num2 = int(nums['drugi'])
        sign = nums['sign']
        result = num1 + num2
        if sign == 'minus':
            result = num1 - num2
        return json.dumps({'result': result})

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')
