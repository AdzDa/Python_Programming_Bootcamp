from flask import Flask, jsonify, render_template
import pswd #calling another script like a module(no.py)

app = Flask(__name__, template_folder="templates")

my_Job = "Data Scientist"

#Calling variables from another python script
my_name = pswd.username
my_password = pswd.password

@app.route('/')
def welcome():
    return "Hello World. My name is " + my_name + "! I am a " + my_Job + ". My password is " + my_password 

@app.route('/list') 
def my_list():
    myList = ["Adzrul", "Danin"]
    return myList[0]        #return only a string

@app.route('/listA') 
def my_listA():
    myListA = ["Adzrul", "Danin"]
    return jsonify(myListA)        #this is to return a list(not string)

@app.route('/name/<username>')
def hello(username):
    #create dynamic url
    return "Hello " + username + ", May you have a great day!"

@app.route('/htmlformat')
def index():
    return f"<h1>Hello World! My name is {my_name}</h1>\n<p>This is a paragraph</p>"

@app.route('/multiple_html')
def listing():  #Multiple html lines
    line1 = "<h1><b>Hello</b> World!</h1>"
    line2 = "<p>If music be the food of love, play on!</p>"
    line3 = "<img src='https://media.giphy.com/media/sWrDT2OqxJ3Fu/giphy.gif''>"
    total = line1+line2+line3
    return total

@app.route('/index')
def read_html():
    return render_template('indexA.html')

if __name__ == '__main__':
    app.run(debug = True)