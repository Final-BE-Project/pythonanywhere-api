
from flask import Flask, jsonify, request
import ast
app = Flask(__name__)


@app.route('/postData', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting': 'Hello from Flask!'}
        response = jsonify(message)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    # POST request
    if request.method == 'POST':
        data = request.get_data()
        data = ast.literal_eval(data.decode('utf-8'))

        with open("index.html", "w") as file:
            file.write(str(data))
        message = {'greeting': 'Hello from Flask!'}
        response = jsonify(message)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


app.run(debug=True)
