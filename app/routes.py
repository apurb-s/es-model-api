from flask import Blueprint, request, jsonify
from .model import predict

main = Blueprint('main', __name__)

@main.route('/miniFuturesPredict', methods=['POST'])
def prediction_route():
    data = request.get_json()
    prediction, probability = predict(data)
    return jsonify({'prediction': prediction, 'probability': probability})
