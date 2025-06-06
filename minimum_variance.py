from flask import Flask, request, jsonify
from domain.temp import main

app = Flask(__name__)


@app.route('/')
def minimum_variance():
    return 'Hello, World!'

@app.get("/minimum-portfolio")
def get_countries():
    testminportfolio = main()
    return testminportfolio