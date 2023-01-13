from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SESSION_TYPE'] = "filesystem"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template('index.html')

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("HI " + str(request.form['name_input']) + ", greate to see you!")
	return render_template('index.html')
	