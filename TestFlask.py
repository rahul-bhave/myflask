import flask
from flask import Flask, request, jsonify, abort, render_template
app = Flask(__name__)

@app.route("/")
def say_hello():
   "My first app"
   return render_template('index.html')

if __name__ == "__main__":
   app.run(host="127.0.0.1", port=5000, debug=True)