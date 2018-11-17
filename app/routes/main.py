
from flask import request, render_template, jsonify
from app import app
from app.utils.main import helloWorld, handleFile, allowed_file


@app.route('/', methods=['GET', 'POST'])
def index():

    response = {}

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if 'file' not in request.files:
            response['error'] = 'No file part'

            return jsonify(response)

        f = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if f.filename == '':
            response['error'] = 'No selected file'

            return jsonify(response)

        if not allowed_file(f.filename):
            response['error'] = 'Filetype not allowed'

            return jsonify(response)

        if f and allowed_file(f.filename):
            response = handleFile(f)
        
            return jsonify(response)


@app.route("/hello-world")
def hello():
    response = helloWorld()

    return jsonify({'response': response})