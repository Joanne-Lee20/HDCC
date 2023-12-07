from flask import Flask, render_template
import csv

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
    ("aesthetics", "AI Aesthetics",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("emotion", "AI Emotions and Sentiment",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("education", "AI Education",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("privacy", "AI Privacy and Cybersecurity",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("bias", "AI Bias and Discrimination",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("datasets", "AI Datasets",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("ethics", "AI Ethics",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),
    ("labor", "AI Labor",           
        "author names here?", "love words that are directed towards people. some summary here",
        "https://example.com"),]

@app.route('/research_papers')
def research_papers():
    return render_template("research_papers.html", papers = research_papers_content)

resources_content = []
media_types = set()
topics = set()
images = {
    "Book": "https://static.vecteezy.com/system/resources/previews/024/043/963/non_2x/book-icon-clipart-transparent-background-free-png.png",
    "Academic paper or report": "https://cdn-icons-png.flaticon.com/512/11469/11469020.png",
    "Online course": "https://cdn-icons-png.flaticon.com/512/10650/10650916.png",
    "Video": "https://cdn-icons-png.flaticon.com/512/4237/4237875.png",
    "Website or blog": "https://cdn-icons-png.flaticon.com/512/5044/5044729.png",
    "Podcast": "https://cdn-icons-png.flaticon.com/512/2628/2628834.png",
    "Online article": "https://cdn-icons-png.flaticon.com/512/4104/4104700.png",
    "Organization": "https://cdn-icons-png.flaticon.com/512/2980/2980016.png",
    "TED Talk": "https://cdn-icons-png.flaticon.com/512/3200/3200680.png"
}

with open("static/resources.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        resources_content.append(line)
        media_types.add(line['Platform/Media Type'])
        topics.add(line['Topic'])

topics.remove("")

@app.route('/resources')
def resources():
    return render_template("resources.html", resources_content = resources_content, images = images,
                           media_types = list(media_types), topics = list(topics))

@app.route('/syllabus')
def syllabus():
    return render_template("syllabus.html")

@app.route('/workshop_projects')
def workshop_projects():
    return render_template("workshop_projects.html")

if __name__ == '__main__':
    app.run(debug=True)
