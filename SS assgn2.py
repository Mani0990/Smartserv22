import flask
from flask import request, jsonify

@app.route('/api/v1/resources/books/all', methods=['GET'])
def home():
    return jsonify(books)


app = flask.Flask(__name__)
app.config["DEBUG"] = True