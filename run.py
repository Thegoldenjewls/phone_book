#     You need the recreate the following:
# Create a virtural Environment 
# Install requirements in the environment (flask, python-dotenv, etc.)
# Install Flask-WTF (Form Validation)
# Create the basic file structure for a flask package (app folder -> __init__, routes, forms, etc.)
# Create a home route for the home page
# Create the "Register Phone Number" route
#     - Display a form that will take in the following information:
#          - Name
#          - Phone Number
#          - Address
#     - On form submit, print out the user info 
#          * For added bonus, Flash a message with the new user info

# Links for reference
# Flask Documentation
# Flask-WTF

# GitHub repository to Kekambas Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"