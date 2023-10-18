from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__, template_folder="templates")

recipe = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?f=a&authuser=0")
food_cal = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list?api_key=MXmAamnHdoV8eL6XkXoPtkh5FTzlZO7arnzU7bc8&authuser=0")   #food_cal=Food's Calories

@app.route('/')
def read_html():
    return render_template('indexA.html')

@app.route('/recipe')
def find_recipe()
    return

@app.route('/calorie')
def calorie()
    return

if __name__ == '__main__':
    app.run(debug = True)