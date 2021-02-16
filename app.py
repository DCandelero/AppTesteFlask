from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from json import dumps
from ConvertBase64audioToText import base64audio_to_text

# set flask and recover db file
app = Flask(__name__)
api = Api(app, errors=errors)

class Home(Resource):
    def get(self):
        return "Deu bom"

#  Map endpoints
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

