from flask import Flask
from gpiozero import LED

led = LED(17)
app = Flask(__name__)

@app.route('/')
def hello_piCAN():
    led.off()
    return 'Hello, from piCAN!'

@app.route('/on')
def piCAN_on():
    led.on()
    return 'led on'

@app.route('/off')
def piCAN_off():
    led.off()
    return 'led off'

@app.route('/blink')
def piCAN_blink():
    led.blink()
    return 'led blink'
