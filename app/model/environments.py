import logging
from flask_restful import Resource
from controller import environments

class main(Resource):
    def get(self):
        

class healthz(Resource):
    def get(self):
        return {'Status': 'Some body call for the exterminator?'}