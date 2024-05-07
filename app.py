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
        "Associate Professor, Department of Art",
        "Does AI hold its own against generative art and digital media? Where might it synergize?",
        "dQw4w9WgXcQ"),
    ("Professor Trevor Muñoz",
        "Director of the Maryland Institute for Technology in the Humanities",
        "What role might AI play in the world of digital humanities and community heritage?",
        "dQw4w9WgXcQ"),
    ("Professor José Calderón",
        "Lecturer, Department of Computer Science and Instructor, DCC",
        "<i>\"Maybe 'Artful Insincerity.'\"</i>",
        "dQw4w9WgXcQ"),
    ("Dr. Hal Daumé & Dr. Katie Shilton",
        "Professor, Department of Computer Science (Daumé) | Associate Professor, College of Information Studies (Shilton)",
        "dQw4w9WgXcQ"),
    ("Dr. John Horty",
        "Professor, Department of Philosophy",
        "dQw4w9WgXcQ"),
    ("Dr. Dan Greene",
        "Associate Professor, College of Information Studies",
        "dQw4w9WgXcQ"),
    ("Dr. Marisa Parham",
        "Professor, Department of English, Director of the African American Digital and Experimental Humanities Initiative",
        "dQw4w9WgXcQ"),
    ("Dr. Jing Liu",
        "Assistant Professor, School of Education",
        "description",
        "dQw4w9WgXcQ"),
    ("Professor Irina Muresanu",
        "Associate Professor, School of Music",
        "dQw4w9WgXcQ"),
    ("Dr. Furong Huang",
        "Assistant Professor, Department of Computer Science",
        "dQw4w9WgXcQ"),
    ("Dr. Sheena Erete",
        "Associate Professor, School of Information",
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
    ("aesthetics", "Aesthetics & Creativity",           
        "Demilade Kayode, Fola Agbebi, Kaitlyn Ray, Dua Naqvi, Natalie Gaitan, Habib Camara", "\"Creativity is all around us...\"",
        "https://drive.google.com/file/d/1FFl3bB5GyrnvN1tdAkAJYzSPx4_ihTrA/view?usp=sharing"),
    ("ecology",  "AI + Ecology",          
        "Aashika, Ash, Austin, Karima, Ray", "\"AI has the potential to play a crucial role...\"",
        "https://drive.google.com/file/d/1l93Ck-z0a7DpLbUDK1yFstM6ua6wnuEE/view?usp=sharing"),
    ("advocacy", "AI Advocacy: Politics and Progress",           
        "Javier Fuentes, Michelle Berry, Reese Artero, Sofia V. Santiago, Sarah Hajjar, Purva Jani", "\"Started in 2020 by the Trump Administration...\"",
        "https://drive.google.com/file/d/1_Y0a-IQVFo9myCH81RvCRbyTVXywA50V/view?usp=sharing"),
    ("education", "AI in Education",           
        "Aleeza Malik, Meredith Hecht, Kimora Brown-Lawrence, Esther Ou, Anna Lee, Noelia Gonzalez, Sravya Patibandla", "\"Recent developments in AI are redefining what education means...\"",
        "https://drive.google.com/file/d/1HO6J06_P-OYPy2Na4_mG3Az6XqQZbN96/view?usp=sharing"),
    ("privacy", "AI Privacy and Cybersecurity",           
        "Nathaniel Unnikumaran, Sylvia Vallina, Ethan Yen", "\"Currently, AI is being used on one end to...\"",
        "https://drive.google.com/file/d/1UWqxvFF63m_xVaqY36vwQ9IEWf5oPU51/view?usp=sharing"),
    ("culture",  "AI's Harmonious Fusion",
        "Basmah E, Cynthia A, Katherine B, Mia S, Morgan B, Reza A.", "\"Through the creation of AI and the mass production of subsequent...\"",
        "https://drive.google.com/file/d/1iLI3MMm9HEov4HOG9aGeGRW8ZdRjZOu1/view?usp=sharing"),
    ("emotion", "AI's Quest to Decipher: Emotions and Sentiment",           
        "Stella Colantuno, Utkarsh Gupta, Simon Osgood, Shiham Siddiqui, Adam Zennia", "\"In lines of code, AI's silent quest...\"",
        "https://drive.google.com/file/d/1_q2_aqQg-Kn59TNewG43KKSh2YK2RK0V/view?usp=sharing"),
    ("bias", "Bias and Discrimination in Artificial Intelligence",           
        "Andie Sjaarda, Anthony Urbina, Ariel Zang, Eva Kumits, Farah Mikdashi, Grace Magny-Fokam, Sami Kudagunti", "\"With the fast-rising prevalence of AI systems...\"",
        "https://drive.google.com/file/d/1thYwvLbx33yagJBeV8FtuLlANf7WdHM9/view?usp=sharing"),
    ("datasets", "Datasets in Generative AI",           
        "Diego Abarcar-Calugay, Joanne Lee, Valerie Lin, Jude Lwin, Sunil Pateel, Cathy Wu", "\"It cannot be understated how important datasets are...\"",
        "https://drive.google.com/file/d/17ow19-zu_vC3tSKReSZZwICP1uRkpg-r/view?usp=sharing"),
    ("ethics", "Ethics & Values Alignment",           
        "Lydia Chan, Elliot Gerig, Priya Nayak, Tracy Tan, Emma Wilson, Brian Wu, Frederick Zheng", "\"AI ethics are a set of values, principles, and techniques that employ...\"",
        "https://drive.google.com/file/d/1uPp129J8eaFbQSB5f7H6dxV0LriXHhNZ/view?usp=sharing"),
    ("labor", "Labor & AI",           
        "Nina Butler, Romi Radi, Finna Hsu, Kevin Qi", "\"Automation has been used in society for years...\"",
        "https://drive.google.com/file/d/1TpsNY1dUHTompGufQHrgBOqFOus9O0Q6/view?usp=sharing"),
    ]

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
    app.run()
