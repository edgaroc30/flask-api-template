# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Api
from model import main

app = Flask(__name__)
api = Api(app)

api.add_resource(main.healthz, '/healthz')
api.add_resource(main.main, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')