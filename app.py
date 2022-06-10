from flask import (Flask,
                   render_template)
from utils import (load_candidates,
                   get_candidate_by_id,
                   get_candidates_by_skill,
                   get_candidates_by_name)

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:id>")
def page_candidate_by_id(id):
    candidate = get_candidate_by_id(load_candidates(), id)
    return render_template('card.html', candidate=candidate)


@app.route("/skills/<skill>")
def page_candidates_by_skill(skill):
    candidates = get_candidates_by_skill(load_candidates(), skill)
    return render_template('skill.html', skill=skill, candidates=candidates)


@app.route("/search/<name>")
def page_candidates_by_name(name):
    candidates = get_candidates_by_name(load_candidates(), name)
    return render_template('search.html', name=name, candidates=candidates)


if __name__ == '__main__':
    app.run()
