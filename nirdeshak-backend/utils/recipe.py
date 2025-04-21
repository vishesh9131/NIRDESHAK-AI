from models.tinyllama_inference import run_tinyllama

def get_suggestion(data):
    ingredients = data.get('ingredients', '')
    prompt = f"Suggest a simple and tasty recipe using these ingredients: {ingredients}"
    response = run_tinyllama(prompt)
    return {"recipe_suggestion": response}
