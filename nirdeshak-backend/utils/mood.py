from models.tinyllama_inference import run_tinyllama

def get_boost(data):
    mood_input = data.get('mood', 'I feel low')
    prompt = f"I'm feeling {mood_input}. Can you say something to lift my spirits?"
    response = run_tinyllama(prompt)
    return {"mood_boost": response}
