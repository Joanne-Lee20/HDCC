from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bestpractices')
def bestpractices():
    return render_template("bestpractices.html")

research_papers_content = [
    ("ecology",  "AI + Ecology",           "author names here?", "love trees. some summary here"),
    ("culture",  "AI's Harmonious Fusion", "author names here?", "love words. some summary here"),
    ("advocacy", "AI Advocacy",            "author names here?", "love words that are directed towards people. some summary here"),
]
@app.route('/research_papers')
def research_papers():
    return render_template("research_papers.html", papers = research_papers_content)

if __name__ == '__main__':
    app.run(debug=True)
