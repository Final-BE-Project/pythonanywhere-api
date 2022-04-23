
from flask import Flask, jsonify, render_template, request
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
        print(data)
        # with open("index.html", "w") as file:
        # file.write(str(data))
        message = {'message': data+' from Flask!'}
        response = jsonify(message)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
