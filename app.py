from flask import Flask, render_template, request, jsonify 
import json 
app = Flask(_name_) 
# Load recipes from JSON 
with open('recipes.json') as f: 
    recipes = json.load(f) 
@app.route('/') 
def home(): 
    conditions = list(set([recipe['condition'] for recipe in recipes])) 
    return render_template('index.html', conditions=conditions) 
@app.route('/get_recipe', methods=['POST']) 
def get_recipe(): 
    condition = request.form['condition'] 
    condition_recipes = [recipe for recipe in recipes if recipe['condition'] == condition] 
    return render_template('recipe.html', condition=condition, recipes=condition_recipes) 
@app.route('/submit_feedback', methods=['POST']) 
def submit_feedback(): 
    feedback = request.form['feedback'] 
    print(f"Feedback received: {feedback}")  # Log feedback to console 
    return render_template('feedback_thankyou.html', feedback=feedback) 
if _name_ == '_main_': 
    app.run(debug=True)