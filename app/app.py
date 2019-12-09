# app.py - a minimal flask api using flask_restful
import logging
logging.basicConfig(#format='%(levelname)s: %(asctime)s %(funcName)s(%(lineno)d) %(message)s',
                    filemode='w',
                    filename='logs/output.log',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
from flask import Flask
from flask_restful import Api

from model import main,environment_manager

environment_manager.environment
app = Flask(__name__)
api = Api(app)

api.add_resource(main.healthz, '/healthz')
api.add_resource(main.main, '/')
api.add_resource(environment_manager.environment,'/environment')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')