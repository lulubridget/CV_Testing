from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {'id':1,
     'title': 'Actor',
     'location': 'Switherland',
     'Age': '20'},
    {'id':2,
     'title': 'Singer',
     'location': 'China',
     'Age': '15'},
    {'id':3,
     'title': 'Dancer',
     'location': 'Japan',
     'Age': '10'},
    {'id':4,
     'title': 'Musician',
     'location': 'Norway',
     'Age': '25'},
    {'id':5,
     'title': 'Musician',
     'Age': '7'},
]
#option 1 to dynamic data with html
@app.route('/')
def home():
    return render_template("index.html", idealJobs=jobs, name = 'Lu')

#option 2 to dynamic data with json 
@app.route('/api/jobs')
def list_joba():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug = True)
