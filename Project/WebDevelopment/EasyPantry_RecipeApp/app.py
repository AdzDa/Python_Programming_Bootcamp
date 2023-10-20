#import package and modules
from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
import sorry_line   #import sorry_line.py file

app = Flask(__name__, template_folder="templates")

#Calling variables from another python script
apologize = sorry_line.sorry

# Call the API by opening the URL and reading the data.
recipes_collection = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?f=a&authuser=0")
food_cal_info = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list?api_key=MXmAamnHdoV8eL6XkXoPtkh5FTzlZO7arnzU7bc8&authuser=0")   #food_cal_info=Food's Calories

# Decode the raw JSON data.
# Convert JSON as a dictionary format
response_recipes = recipes_collection.json()
response_calories = food_cal_info.json()


recipe_ingredient = {}  #Global empty(initial) dictionary for recipe or ingredients' input

#Common rendering html file
@app.route('/') #ok
def home_page():
    return render_template('index.html')


#half ok
@app.route('/recipe_page_ui', methods = ['POST', 'GET'])  # url routing model
def recipe_page_UI():
    if  request.method == 'POST':
        #Assigning new variable for the values/ info obtained from the form
        recipe_page_input_txt = request.form["input_text"]
        searchBTN = request.form["search_btn"]
        recipe_ingredient["recipe_page_input_txt"] = recipe_page_input_txt
        recipe_ingredient["searchBTN"] = searchBTN
        return redirect(url_for('show_recipes'))
    else:    
        return render_template('recipes.html')


@app.route('/show_recipes') #half ok
def show_recipes(recipe_page_input_txt):
    i = 0
    while i < 4:
        if recipe_ingredient["recipe_page_input_txt"] == response_recipes["meals"][i]["strMeal"]:
            return render_template("show_recipes.html", meal = response_recipes["meals"][i]["strMeal"], recipe_process = strInstructions[i])
        i += 1


# Just to show what meals' recipes included
@app.route('/meals_info_provided')  #ok
def meals_included():
#multiple list 
    l1 = response_recipes["meals"][0]["strMeal"] 
    l2 = response_recipes["meals"][1]["strMeal"] 
    l3 = response_recipes["meals"][2]["strMeal"] 
    l4 = response_recipes["meals"][3]["strMeal"] 
    total = f"{l1} / {l2} / {l3} / {l4}"  
    return (total)



@app.route('/ingredient_registered')    #ok
#check the list of regitered ingredients only
def registered_ingredients():
    ingredients = []    #Assigning ingrdients variable as an empty list (initial) 
    #originally; strIngredient1 to strIngredient20 
    #but the max used/ has values are up-to strIngredient13 only
    #& only 4 meals registered in the API
    for i in range(4):  #Nested for loops
        for j in range(13):
            e ="strIngredient"+str(j+1)     # eg: strIngredient1
            ingredients.append(response_recipes["meals"][i][e])
    return jsonify(ingredients)    #this is to return a list(not string)


@app.route('/<meal>')   #ok
#create dynamic url; meal input will be used in the code below to check if the meal is registered. If yes, then the instruction will be printed
def recipe_instruction_1(meal):
    i = 0
    while i < 4:
        if meal == response_recipes["meals"][i]["strMeal"]:
            a = response_recipes["meals"][i]["strInstructions"]
            return (f"The cooking instruction is as below: \n\t {a}")
        i += 1


#if input is ingredient; then, print out what possible recipe
@app.route('/recipe_generator')
def recipe_gen():   #ok
    ingredient = input("Please enter related ingredient: ")
    strIngredients = []     #empty list of strIngredients
    for i in range(4):
        for j in range(13):
            e ="strIngredient"+str(j+1)     # eg: strIngredient1
            strIngredients.append(response_recipes["meals"][i][e])  #append strIngredients list with values from response_recipes["meals"][i][e]; starting at 0 index
            a = strIngredients[j]
            if ingredient == a:
                b = response_recipes["meals"][i]["strInstructions"]
                return (b)
            else:
                return (apologize)  #Reading/ calling back the sorry_line.py file --> ok




@app.route('/health/food_registered')    
#check the list of regitered foods only (Nutritional info)
def registered_food_nutrient():
    food = []    #Assigning food variable as an empty list (initial) 
    for i in range(len(response_calories)):
        food.append(response_calories[i]["description"])    #add new item in food list
    return jsonify(food)


@app.route('/health/food_kcal/<what_food>')    
#create dynamic url; what_food input is based on food_registered
def kcal(what_food):    #call/ get argument from the url
    for i in range(len(response_calories)):
        if what_food == response_calories[i]["description"]
            a = response_calories[i][""]
            return f"The Energy in {what_food} is {a} kcal"



if __name__ == '__main__':
    app.run(debug = True)