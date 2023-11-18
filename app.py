from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'bethechange'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    """Render Madlibs form"""

    return render_template('form')
    

@app.route('/madlib')
def generate_madlib():
    """Render Madlib with submitted words"""
    
    verb = "ran"
    return render_template('madlib', verb=verb)