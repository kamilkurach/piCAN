from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import IPs as ip
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome_and_grant_token():
    if request.method == 'GET':
        return render_template("public/welcome.html")
    
    if request.method == 'POST':
        return redirect(url_for('main'))

@app.route('/main', methods=['POST'])
def piCAN_main():
    if request.method == 'POST':
        try:
            r = requests.get(ip.MAIN_PAGE)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/on', methods=['POST'])
def piCAN_on():
    if request.method == 'POST':
        try:
            r = requests.get(ip.ON)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/off', methods=['POST'])
def piCAN_off():
    if request.method == 'POST':
        try:
            r = requests.get(ip.OFF)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/blink', methods=['POST'])
def piCAN_blink():
    if request.method == 'POST':
        try:
            r = requests.get(ip.BLINK)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

if __name__ == '__main__':
    app.run()
