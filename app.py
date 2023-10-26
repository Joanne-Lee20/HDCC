from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bestpractices')
def bestpractices():
    return render_template("bestpractices.html")

if __name__ == '__main__':
    app.run(debug=True)