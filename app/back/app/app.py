from flask import Flask, request, Response
from flask_restful import Resource, Api
from time import sleep
import random, time

app = Flask(__name__)
api = Api(app)

class Tracks(Resource):
    def get(self):
        result = (
            "Sieur Devops, le castel est en flammes!", 
            "J'vous ai dit pour le penis du canard?", 
            "Miou-Miou consulte la base de données.",
            "Dans le but de pallier à la baisse de confiance présente, je recommande d’examiner la majorité des hypothèses opportunes, à moyen terme.",
            "Malgré la fragilité de la société, je vous demande d’expérimenter parmi les hypothèses évidentes, dans une perspective correcte.",
            "Et la marmotte fabrique du savon avec la graisse d'un robot qui danse.",
            "Le colonel Moutarde aimerait bien être une tartiflette aux 4 fromages.",
            "Le chocolat chaud fait de nombreuses victimes d'entartrage.",
            "Un lilliputien colle une patate de forain à une 205 turbo diesel.",
            "Eminem se dandine avec un pauvre accordéoniste.",
            "Batman se rase les jambes avec des pailles McDo.",
            "Un geek transpirant regarde dehors, il y voit un poney.",
            "Une vache carnivore s'éternise à cause des champignons.",
            "Tyrion Lannister danse la salsa avec le homard de Dracula.",
            "Une nuée de corbeaux cherche toujours un pot de confiture artisanal.",
            "CanardPC code avec François Hollande."
            )
        sleep (random.uniform(0.5,2.5))
        return Response(random.choice(result), status=200)

api.add_resource(Tracks, '/tracks') 

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')