from flask import Flask, request, Response
from flask_restful import Resource, Api
from time import sleep
import random, time

app = Flask(__name__)
api = Api(app)

class Tracks(Resource):
    def get(self):
        print(self)
        #request.headers['your-header-name']
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
            "CanardPC code avec François Hollande.",
            "Eu égard à l'extrémité intrinsèque, il convient de gérer les principales issues de bon sens, si l'on veut s'en sortir un jour.",
            "Quelle que soit cette rigueur observée, je préconise un audit afin d’anticiper la simultanéité des décisions que nous connaissons, à l'avenir.",
            "Où que nous mène cette inflexion présente, il faut de toute urgence uniformiser la majorité des issues de bon sens, très attentivement.",
            "Dans le cas particulier de la sinistrose générale, il est nécessaire de se préoccuper de la globalité des décisions du futur, de toute urgence.",
            "Si vous voulez mon avis concernant la restriction conjoncturelle, je préconise un audit afin d’essayer la somme des voies déclinables, avec beaucoup de recul.",
            "Tant que durera l'austérité que nous constatons, il serait bon de prendre en considération précisément les problématiques de bon sens, même si nous devons en tirer des conséquences.",
            "Quoi qu'on dise concernant l'orientation qui est la nôtre, je suggère fortement de gérer la majorité des stratégies possibles, en prenant toutes les précautions qui s'imposent.",
            "Tant que durera la situation de ces derniers temps, nous sommes contraints de favoriser parmi les choix emblématiques, parce que la nature a horreur du vide.",
            "Dans le cas particulier de cette rigueur de la société, je vous demande de se souvenir la simultanéité des choix du passé, avec toute la prudence requise.",
            "Compte tenu de la dégradation des moeurs conjoncturelle, nous sommes contraints d’examiner la somme des organisations matricielles imaginables, pour longtemps."
            )
        sleep (random.uniform(0.1,2))
        return Response(random.choice(result), status=200)

api.add_resource(Tracks, '/tracks') 

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')