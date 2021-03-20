from flask import Flask
import IPs as ip
import requests

app = Flask(__name__)

@app.route('/')
def hello_piCAN():
    try:
        r = requests.get(ip.MAIN_PAGE)
        result = "Hello, from piCAN! [STATUS_CODE: {0}]".format(r.status_code)
        return result
    except requests.exceptions.ConnectionError as e:
        raise SystemExit(e)

@app.route('/on')
def piCAN_on():
    try:
        r = requests.get(ip.ON)
        result = "led on [STATUS_CODE: {0}]".format(r.status_code)
        return result
    except requests.exceptions.ConnectionError as e:
        raise SystemExit(e)

@app.route('/off')
def piCAN_off():
    try:
        r = requests.get(ip.OFF)
        result = "led off [STATUS_CODE: {0}]".format(r.status_code)
        return result
    except requests.exceptions.ConnectionError as e:
        raise SystemExit(e)

@app.route('/blink')
def piCAN_blink():
    try:
        r = requests.get(ip.BLINK)
        result = "led blink [STATUS_CODE: {0}]".format(r.status_code)
        return result
    except requests.exceptions.ConnectionError as e:
        raise SystemExit(e)

if __name__ == '__main__':
    app.run()
