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

podcasts_content = [
    ("Professor Brandon Morse",
        "Does AI hold its own against generative art and digital media? Where might it synergize?",
        "dQw4w9WgXcQ"),
    ("Professor Trevor Muñoz",
        "What role might AI play in the world of digital humanities and community heritage?",
        "dQw4w9WgXcQ"),
    ("Professor José Calderón",
        "<i>\"Maybe 'Artful Insincerity.'\"</i>",
        "dQw4w9WgXcQ"),
    ("Dr. Hal Daumé & Dr. Katie Shilton",
        "description",
        "dQw4w9WgXcQ"),
    ("Dr. John Horty",
        "description",
        "dQw4w9WgXcQ"),
    ("Dr. Dan Greene",
        "description",
        "dQw4w9WgXcQ"),
    ("Dr. Marisa Parham",
        "description",
        "dQw4w9WgXcQ"),
    ("Dr. Jing Liu",
        "description",
        "dQw4w9WgXcQ"),
    ("Professor Irina Muresanu",
        "description",
        "dQw4w9WgXcQ"),
    ("Dr. Furong Huang",
        "description",
        "dQw4w9WgXcQ"),
    ("Dr. Sheena Erete",
        "<i>Coming soon...</i>",
        "dQw4w9WgXcQ"),
]
@app.route('/podcasts')
def podcasts():
    return render_template("podcasts.html", episodes = podcasts_content)

@app.route('/polls')
def polls():
    return render_template("pollspage.html")

research_papers_content = [
    ("ecology",  "AI + Ecology",          
        "author names here?", "love trees. some summary here",
        "https://example.com"),
    ("culture",  "AI's Harmonious Fusion",
        "author names here?", "love words. some summary here",
        "https://example.com"),
    ("advocacy", "AI Advocacy",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
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
