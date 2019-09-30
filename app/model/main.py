from flask_restful import Resource

class main(Resource):
    def get(self):
        return {'Hello'}

class healthz(Resource):
    def get(self):
        return {'Status': 'Some body call for the exterminator?'}