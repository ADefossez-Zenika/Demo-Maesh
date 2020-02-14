from flask import Flask,render_template
app = Flask(__name__)
#Import the modules
import requests
import json
import os

if 'WS_URL' in os.environ:
    ws=os.environ['WS_URL']


@app.route('/')
def accueil():
    if 'ws' in locals():
        r = requests.get(ws+"/tracks")
        baratin=r.text
    else:
        baratin="Salut les copains!"
    return render_template('index.html', titre=baratin)

if __name__ == '__main__':
    app.run(host='0.0.0.0')