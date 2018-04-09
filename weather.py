import sys
import Adafruit_DHT
from flask import Flask
from flask import render_template
from flask import redirect
import psutil
#from django.shortcuts import render_to_response

app = Flask(__name__)


@app.route('/')
def index():
    data = Adafruit_DHT.read_retry(11, 21)
    f = (data[1] * (9/5)) + 32
    mem = psutil.virtual_memory()[2]
    c = psutil.cpu_percent()
    return render_template('index.html', variable = data, faren = f, memory = mem, cpu = c)

@app.errorhandler(404)
def page_not_found(e):
    data = Adafruit_DHT.read_retry(11, 21)
    f = (data[1] * (9/5)) + 32
    return render_template('index.html', variable = data, faren = f), 404

if __name__ == "__main__":
    app.run(port=5010)
