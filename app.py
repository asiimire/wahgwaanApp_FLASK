from flask import Flask, render_template, request, flash

app = Flask(__name__)
#the above command creates a class for our app
app.secret_key = "lkjfhrwelh"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template('index.html')

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Wah gwaan " + str(request.form["name_input"]) + ", yuh gud?")
	return render_template('index.html')

	