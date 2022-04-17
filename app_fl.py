from utils import *
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    info = get_info()
    return f"<pre>{get_candidates_list(info)}</pre>"


@app.route("/candidates/<int:x>")
def page_candidates(x):
    info = get_info()
    cand = get_candidate_info(info, x)
    if cand:
        return f"<img src= '{cand['picture']}'><br>" \
               f" {cand['name']}<br> {cand['position']}<br> {cand['skills'].lower()}"
    else:
        return "Такого кандидата не существует."


@app.route("/skills/<x>")
def page_skills(x):
    skills_list_formated = get_candidates_list(get_candidate_skills(get_info(), x))
    return f"<pre>{skills_list_formated}</pre>"


app.run()
