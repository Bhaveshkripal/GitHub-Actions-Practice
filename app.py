# This file is added to the linter check 
from flask import Flask, render_template
app = Flask(__name__)

# adding error to check the linter
if sjds

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
