from flask import Flask, request, Response
from flask_restful import Resource, Api
from time import sleep
import random, time

app = Flask(__name__)
api = Api(app)

class Tracks(Resource):
    def get(self):
        result = ("Shoot to Thrill", "Ain't Talking about Love", "Fuel", "You not Me", "Perfect Strangers")
        sleep (random.uniform(0.5,2.5))
        return Response(random.choice(result), status=200)

api.add_resource(Tracks, '/tracks') 

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')