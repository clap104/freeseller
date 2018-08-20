from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/', methods = ["GET"])
def homepage():
	return render_template("index.html")

@app.route('/how-it-work', methods = ["GET"])
def howitwork():
	return render_template("how-it-work.html")
	
@app.route('/services', methods = ["GET"])
def services():
	return render_template("services.html")
	
@app.route('/contact', methods = ["GET"])
def contact():
	return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug = True)