from flask import Flask
from gpiozero import LED

led = LED(17)
app = Flask(__name__)

@app.route('/')
def hello_chess():
    led.off()
    return 'Hello, from piCAN!'

@app.route('/on')
def hello_chess():
    led.on()

@app.route('/off')
def hello_chess():
    led.off()

@app.route('/blink')
def hello_chess():
    led.blink()
