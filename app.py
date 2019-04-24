from flask import Flask
from flask_restful import Resource, Api 

app = Flask (__name__)

api = Api(app)

class HelloKitten(Resource):
    def get(self):
        return {'cat': 'meow!'}

if __name__ == '__main__':
    app.run(debug=True)