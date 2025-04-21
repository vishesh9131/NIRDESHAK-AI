from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import imaplib
import email
import logging

app = Flask(__name__)

# ========== Logging Setup ==========
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========== Load Model ==========
def load_model():
    try:
        model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Replace with a more capable model if needed
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"  # Requires accelerate
        )
        logger.info("Model loaded successfully.")
        return model, tokenizer
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

model, tokenizer = load_model()

# ========== Generate Response ==========
def tinyllama_response(prompt):
    try:
        full_prompt = (
            f"You are a helpful and knowledgeable AI Assistant. "
            f"Answer the following question concisely and accurately.\n"
            f"User: {prompt}\nAI:"
        )
        inputs = tokenizer(full_prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
        output = model.generate(
            **inputs,
            max_length=512,  # Adjust max_length for concise responses
            do_sample=True,
            temperature=0.7,  # Lower temperature for more deterministic responses
            top_p=0.9        # Adjust top_p for better response diversity
        )
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response.split("AI:")[-1].strip()
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Sorry, I couldn't process your request."

# ========== Routes ==========
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ai', methods=['POST'])
def ai_chat():
    user_input = request.form['user_input']
    logger.info(f"Received AI chat request: {user_input}")
    response = tinyllama_response(user_input)
    return render_template('results.html', user_input=user_input, response=response)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        profile = request.form['profile']
        logger.info(f"Received career recommendation request: {profile}")
        result = tinyllama_response(f"Suggest career options for: {profile}")
        return render_template('recommend.html', result=result)
    return render_template('recommend.html')

@app.route('/mood', methods=['GET', 'POST'])
def mood():
    if request.method == 'POST':
        mood_input = request.form['mood']
        logger.info(f"Received mood booster request: {mood_input}")
        suggestion = tinyllama_response(f"I feel {mood_input}. Give an encouraging suggestion.")
        return render_template('mood.html', result=suggestion)
    return render_template('mood.html')

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        logger.info(f"Received recipe suggestion request: {ingredient}")
        recipe_suggestion = tinyllama_response(f"I have {ingredient}. Suggest a unique recipe.")
        return render_template('recipe.html', result=recipe_suggestion)
    return render_template('recipe.html')

@app.route('/email', methods=['GET', 'POST'])
def email_page():
    if request.method == 'POST':
        email_address = request.form['email']
        password = request.form['password']
        logger.info(f"Received email classification request for: {email_address}")
        results = fetch_and_classify_emails(email_address, password)
        return render_template('email.html', results=results)
    return render_template('email.html')

# ========== Email Classification ==========
def fetch_and_classify_emails(email_address, password):
    try:
        # Connect to the email server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, password)
        mail.select("inbox")

        # Fetch emails
        _, data = mail.search(None, "ALL")
        email_ids = data[0].split()
        emails = []
        for email_id in email_ids[:10]:  # Limit to 10 emails for simplicity
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = msg["subject"]
                    emails.append(subject)

        # Classify emails using the AI model
        results = []
        for email_subject in emails:
            classification = tinyllama_response(f"Classify this email subject: {email_subject}")
            results.append({"subject": email_subject, "classification": classification})

        mail.logout()
        return results
    except Exception as e:
        logger.error(f"Error fetching or classifying emails: {e}")
        return [{"error": "Failed to fetch or classify emails."}]

# ========== Run App ==========
if __name__ == '__main__':
    app.run(debug=True)