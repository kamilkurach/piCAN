from flask import Flask, render_template, request
import IPs as ip
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_piCAN():
    if request.method == 'GET':
        try:
            r = requests.get(ip.MAIN_PAGE)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            raise SystemExit(e)

@app.route('/on', methods=['POST'])
def piCAN_on():
    if request.method == 'POST':
        try:
            r = requests.get(ip.ON)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            raise SystemExit(e)

@app.route('/off', methods=['POST'])
def piCAN_off():
    if request.method == 'POST':
        try:
            r = requests.get(ip.OFF)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            raise SystemExit(e)

@app.route('/blink', methods=['POST'])
def piCAN_blink():
    if request.method == 'POST':
        try:
            r = requests.get(ip.BLINK)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            raise SystemExit(e)

if __name__ == '__main__':
    app.run()
