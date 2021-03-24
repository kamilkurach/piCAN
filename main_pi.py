# test server for operating LED (on, off, blink)

from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import requests
from gpiozero import LED

led = LED(17)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_piCAN():
    if request.method == 'GET':
        try:
            led.off()
            data = {'operation_type': 'off'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e) 

@app.route('/on', methods=['GET'])
def piCAN_on():
    if request.method == 'GET':
        try:
            led.on()
            data = {'operation_type': 'on'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e) 

@app.route('/off', methods=['GET'])
def piCAN_off():
    if request.method == 'GET':
        try:
            led.off()
            data = {'operation_type': 'off'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e) 

@app.route('/blink', methods=['GET'])
def piCAN_blink():
    if request.method == 'GET':
        try:
            led.blink()
            data = {'operation_type': 'blink'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e)

@app.route('/cam01', methods=['GET'])
def piCAN_cam01():
    if request.method == 'GET':
        try:
            return Response(h_func.generate_stream(), mimetype='image/jpeg')
        except requests.exceptions.ConnectionError as e:
            raise SystemExit(0) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
