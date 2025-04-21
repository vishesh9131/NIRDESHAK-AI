from flask import Flask, request, jsonify
from utils import career, mood, recipe, email

app = Flask(__name__)

@app.route('/career', methods=['POST'])
def recommend_career():
    data = request.get_json()
    return jsonify(career.get_recommendation(data))

@app.route('/mood', methods=['POST'])
def boost_mood():
    data = request.get_json()
    return jsonify(mood.get_boost(data))

@app.route('/recipe', methods=['POST'])
def suggest_recipe():
    data = request.get_json()
    return jsonify(recipe.get_suggestion(data))

@app.route('/email', methods=['POST'])
def classify_email():
    data = request.get_json()
    return jsonify(email.classify(data))

if __name__ == '__main__':
    app.run(debug=True)
