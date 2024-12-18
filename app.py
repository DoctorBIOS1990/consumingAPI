from flask import Flask, render_template, request
import requests
from requests.exceptions import ConnectionError

app = Flask(__name__)
#limit = '20'

def constructJSON(categoryChannel, limit):
    try:
        dataObtain = requests.get('https://api.dailymotion.com/videos?channel='+categoryChannel+'&limit='+limit)
        if dataObtain.status_code == 200:
            return dataObtain.json()
        else:
            return {'list': []} 
    except ConnectionError:
        return {'list': []}

@app.route('/')
def index():
    dataJSON = constructJSON('tv','10')
    return render_template('index.html', data=dataJSON['list'])

@app.route('/category', methods=['POST'])
def categoria():
    categoria = request.form['categoria']
    limit = request.form['count']
    dataJSON = constructJSON(categoria, limit)
    return render_template('index.html', data=dataJSON['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
