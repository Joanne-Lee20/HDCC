from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/bestpractices')
def bestpractices():
    return render_template("bestpractices.html")

@app.route('/glossary')
def glossary():
    return render_template("glossary.html")

@app.route('/podcasts')
def podcasts():
    return render_template("podcasts.html")

@app.route('/polls')
def polls():
    return render_template("pollspage.html")

research_papers_content = [
    ("ecology",  "AI + Ecology",           "author names here?", "love trees. some summary here"),
    ("culture",  "AI's Harmonious Fusion", "author names here?", "love words. some summary here"),
    ("advocacy", "AI Advocacy",            "author names here?", "love words that are directed towards people. some summary here"),
]
@app.route('/research_papers')
def research_papers():
    return render_template("research_papers.html", papers = research_papers_content)

resources_content = []
with open("static/resources.txt") as file:
    lines = file.read()
    resources_content = [entry.split('\n') for entry in lines.split('\n\n')]
    resources_content = [entry for entry in resources_content if len(entry) != 1]

@app.route('/resources')
def resources():
    return render_template("resources.html", resources_content = resources_content)

@app.route('/syllabus')
def syllabus():
    return render_template("syllabus.html")

@app.route('/workshop_projects')
def workshop_projects():
    return render_template("workshop_projects.html")

if __name__ == '__main__':
    app.run(debug=True)
