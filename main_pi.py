# test server for operating LED (on, off, blink)

from flask import Flask
from gpiozero import LED

led = LED(17)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_piCAN():
    led.off()
    return 'Hello, from piCAN!'

@app.route('/on', methods=['GET'])
def piCAN_on():
    led.on()
    return 'led on'

@app.route('/off', methods=['GET'])
def piCAN_off():
    led.off()
    return 'led off'

@app.route('/blink', methods=['GET'])
def piCAN_blink():
    led.blink()
    return 'led blink'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
