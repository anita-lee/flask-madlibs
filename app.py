from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def show_questions():
    prompts = silly_story.prompts
    print("prompts =", prompts)

    return render_template("questions.html", prompts_list=prompts)

@app.get('/results')
def add_results():
    prompts = silly_story.prompts
    # prompts_data = [(prompt,request.form.get(prompt)) for prompt in prompts]
    # prompts_dict = dict(prompts_data)

    # prompts_dict = {prompt:request.form.get(prompt) for prompt in prompts}
    # print(request.form)

    story = silly_story.generate(request.args)


    return render_template("story.html", story_text=story)