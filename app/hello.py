from flask import Flask, render_template, jsonify
from datetime import datetime
import socket

from flask.json import JSONDecoder

app = Flask(__name__)

#@app.route("/app")
#def index():
#  return render_template("public/index.html")

@app.route("/")
def main():
  hostName = socket.gethostname()
  date = datetime.today().strftime('%d/%m/%Y - %H:%M:%S')
  return jsonify(
    {
      "hostname": hostName,
      "date" : date
    }
  )

@app.route("/health")
def health():
  return "Online"