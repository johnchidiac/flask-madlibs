
from flask import Flask, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 999
toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_story_select():
    """Show a dropdown menu to select the story to use"""
    titles = [story['title'] for story in stories.mad_libs]
    return render_template('select.jinja-html', titles=titles)

@app.route('/form', methods=["POST"])
def show_form():
    """Render Madlibs form"""
    story_id = int(request.form['title'])
    selected_story = stories.mad_libs[story_id]
    # breakpoint()
    return render_template('form.jinja-html', story_id=story_id, prompts=selected_story['prompts'])

@app.route('/story', methods=["POST"])
def generate_story():
    """Render story with submitted words"""
    data = request.form
    data = data.to_dict()
    new_story_id = int(data['story_id'])
    (k := next(iter(data)), data.pop(k)) # Remove first item from dictionary (story_id) as it is not used in generating story
    new_story_prompts = stories.mad_libs[new_story_id]['prompts']
    new_story_template = stories.mad_libs[new_story_id]['story']
    new_story = stories.Story(new_story_prompts, new_story_template)
    new_story_text = new_story.generate(data)
    return render_template('madlib.jinja-html', story=new_story_text)