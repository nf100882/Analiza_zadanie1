from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    # Pobranie wartości z query string (domyślnie 0, jeśli brak)
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    except ValueError:
        return jsonify({"error": "Wartości muszą być liczbami."}), 400

    # Reguła decyzyjna
    sum_value = num1 + num2
    prediction = 1 if sum_value > 5.8 else 0

    # Przygotowanie odpowiedzi
    response = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2,
            "sum": sum_value
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
