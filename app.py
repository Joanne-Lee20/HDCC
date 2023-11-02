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

@app.route('/research_papers')
def research_papers():
    return render_template("research_papers.html")

if __name__ == '__main__':
    app.run(debug=True)
