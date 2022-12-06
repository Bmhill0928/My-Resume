# Import necessary packages and functions
from flask import Flask, render_template

# Create our web application
app = Flask(__name__)

# Create our routes
@app.route('/')
def resume():
	return render_template("index.html")