from flask import Flask, request, jsonify
from domain.services import minimum_varience_service as min_var

app = Flask(__name__)


@app.route('/')
def endpoint_definitions():
    return 'Hello, World!'

@app.post("/minimum-portfolio")
def post_minimum_portfolio():
    http_body = request.get_json()

    try:
        asset_elements = http_body.get("AssetInformation", [[]])
        correlation = http_body.get("Correlation", [[]])
        expected_return = http_body.get("ExpectedReturn", float)

        min_var_complete = min_var.current_minimum_variance_service(
            correlation=correlation, assets=asset_elements, expected_return=expected_return
        )

        return jsonify(min_var_complete)

    except Exception as e:
        app.logger.info(f"This request has thrown an error: {e}")
        return None
