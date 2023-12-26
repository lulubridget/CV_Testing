from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)

    
#option 1 to dynamic data with html
@app.route('/')
def home():
    jobs_list = load_jobs_from_db()
    print(jobs_list)
    return render_template("index.html", idealJobs=jobs_list, name = 'Lu')

##option 2 to dynamic data with json 
# @app.route('/api/jobs')
# def list_joba():
#     return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug = True)
