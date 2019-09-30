# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class main(Resource):
    def get(self):
        return {'Hello'}

class healthz(Resource):
    def get(self):
        return {'Status': 'Some body call for the exterminator?'}

api.add_resource(healthz, '/healthz')
api.add_resource(main, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')