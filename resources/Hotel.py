from flask_restful import Resource


class Hotels(Resource):
    def get(self):
        return {'hotels': 'My Hotels'}
