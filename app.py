from flask_cors import CORS
import google.generativeai as genai
import logging

from flask import Flask, request, render_template, jsonify
from gem import GEM

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure API key
genai.configure(api_key=GEM)

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-pro")

# Dictionary to store chat sessions by ID
chat_sessions = {}

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ai', methods=['POST'])
def ai_chat():
    user_input = request.form['user_input']
    logger.info(f"Received AI chat request: {user_input}")
    response = gemini_response(user_input)
    
    # Check if request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'response': response})
    
    return render_template('results.html', user_input=user_input, response=response)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        profile = request.form['profile']
        logger.info(f"Received career recommendation request: {profile}")
        result = gemini_response(f"Suggest career options for: {profile}")
        
        # Check if request is AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'result': result})
            
        return render_template('recommend.html', result=result)
    return render_template('recommend.html')

@app.route('/mood', methods=['GET', 'POST'])
def mood():
    if request.method == 'POST':
        mood_input = request.form['mood']
        logger.info(f"Received mood booster request: {mood_input}")
        suggestion = gemini_response(f"I feel {mood_input}. Give an encouraging suggestion.")
        
        # Check if request is AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'result': suggestion})
            
        return render_template('mood.html', result=suggestion)
    return render_template('mood.html')

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        logger.info(f"Received recipe suggestion request: {ingredient}")
        recipe_suggestion = gemini_response(f"I have these ingredients: {ingredient}. Suggest a unique recipe that uses them. Include ingredients list and step by step instructions.")
        
        # Check if request is AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'result': recipe_suggestion})
            
        return render_template('recipe.html', result=recipe_suggestion)
    return render_template('recipe.html')

def gemini_response(prompt, chat_id='default'):
    # Get or create chat session for this ID
    if chat_id not in chat_sessions:
        chat_sessions[chat_id] = model.start_chat(history=[])
    
    chat = chat_sessions[chat_id]
    
    try:
        # Send the message and get a response
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Sorry, I couldn't process your request."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)