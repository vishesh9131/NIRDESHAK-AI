from models.tinyllama_inference import run_tinyllama

def get_recommendation(data):
    prompt = f"Suggest a career path for someone with this background: {data['education']}"
    response = run_tinyllama(prompt)
    return {"career_recommendation": response}
