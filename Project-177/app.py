from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates=[
    {
        "inputs":5,
        "category":"games",
        "word":"chess"
    },
    {
        "inputs":6,
        "category":"countries",
        "word":"france"
    },
    {
        "inputs":6,
        "category":"colours",
        "word":"yellow"
    }
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status":"success",
        "word": random.choice(templates)
    })