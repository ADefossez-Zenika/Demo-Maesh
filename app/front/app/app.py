from flask import Flask,render_template
app = Flask(__name__)
#Import the modules
import requests
import json
import os

ws=os.environ['WS_URL']

@app.route('/')
def accueil():
    r = requests.get(ws+"/tracks")
    return render_template('index.html', titre=r.text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')