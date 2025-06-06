from flask import Flask, request, jsonify
from domain.temp import main

app = Flask(__name__)


@app.route('/')
def endpoint_definitions():
    return 'Hello, World!'

@app.post("/minimum-portfolio")
def post_minimum_portfolio():
    http_body = request.get_json()

    app.logger.info(http_body)

    try:
        asset_elements = http_body.get("AssetInformation", [[]])
        covariance = http_body.get("Covariance", [[]])

        min_var_portfolio = main(testCor=covariance, testEr=asset_elements)

        return min_var_portfolio

    except Exception as e:
        print(f"This request has thrown an error")
        return None

