# test server for operating LED (on, off, blink)

from flask import Flask
from flask import request
from flask import jsonify
from gpiozero import LED
import helper_functions as h_func

led = LED(17)
app = Flask(__name__)
h_func.GPIO_setup()

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

@app.route('/360_cw', methods=['GET'])
def piCAN_360_clockwise():
    if request.method == 'GET':
        try:
            h_func.do_360_clockwise()
            data = {'operation_type': '360_clockwise'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e) 

@app.route('/360_ccw', methods=['GET'])
def piCAN_360_counter_clockwise():
    if request.method == 'GET':
        try:
            h_func.do_360_counter_clockwise()
            data = {'operation_type': '360_counter_clockwise'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e) 

@app.route('/90_cw', methods=['GET'])
def piCAN_90_clockwise():
    if request.method == 'GET':
        try:
            h_func.do_90_clockwise()
            data = {'operation_type': '90_clockwise'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e) 

@app.route('/90_ccw', methods=['GET'])
def piCAN_90_counter_clockwise():
    if request.method == 'GET':
        try:
            h_func.do_90_counter_clockwise()
            data = {'operation_type': '90_counter_clockwise'}
            return jsonify(data), 200
        except gpiozero.GPIOZeroError as e:
            raise SystemExit(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
