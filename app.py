from flask import Flask, render_template, request
import requests

app = Flask(__name__)
limit = '20'

def constructJSON(categoryChannel):
    dataObtain = requests.get('https://api.dailymotion.com/videos?channel='+categoryChannel+'&limit='+limit)
    return dataObtain.json()

@app.route('/')
def index():
    dataJSON = constructJSON('tv')
    return render_template('index.html', data = dataJSON['list'])

@app.route('/category', methods=['POST'])
def categoria():
    categoria = request.form['categoria']
    dataJSON = constructJSON(categoria)
    return render_template('index.html', data = dataJSON['list'])

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8000, debug = True)
 