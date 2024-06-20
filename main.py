from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_all_candidates():
    all_candidates = get_all()
    return f'<pre> {all_candidates} </pre>'


@app.route("/candidates/<int:pk>")
def page_candidate(pk):
    picture, candidate = get_by_pk(pk)
    return f"<img src = {picture}> <pre> {candidate} </pre>"


@app.route("/skills/<name>")
def page_candidates_by_skill(name):
    candidates_by_skill = get_by_skill(name)
    return f"<pre> {candidates_by_skill} </pre>"


app.run()
