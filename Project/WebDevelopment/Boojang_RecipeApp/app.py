from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder="templates")

recipes_collection = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?f=a&authuser=0")
food_cal_info = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list?api_key=MXmAamnHdoV8eL6XkXoPtkh5FTzlZO7arnzU7bc8&authuser=0")   #food_cal_info=Food's Calories

recipe_ingredient = {}  #Global empty(initial) dictionary for recipe or ingredients' input

@app.route('/', methods = ['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        lastName = request.form["lname"]
        recipe_ingredient["lastName"] = lastName
        return redirect(url_for('recipes'))
    else:    
        return render_template('index.html')

@app.route('/recipes')
def find_recipes():
    return render_template('recipe.html', recipes=recipe_ingredient["recipe"])

@app.route('/calorie')
def calorie():
    return

if __name__ == '__main__':
    app.run(debug = True)