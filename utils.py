import json

CANDIDATES_FILE = 'candidates.json'


def _load_json_file(filename):
    with open(filename) as file:
        return json.load(file)


def load_candidates():
    return _load_json_file(CANDIDATES_FILE)


def get_candidate_by_id(candidates, id):
    for candidate in candidates:
        if candidate['id'] == id:
            return candidate
    return None


def get_candidates_by_skill(candidates, skill):
    candidates_with_skill = []
    for candidate in candidates:
        skills = [skill.lower().strip() for skill in candidate['skills'].split(',')]
        if skill.lower() in skills:
            candidates_with_skill.append(candidate)
    return candidates_with_skill


def get_candidates_by_name(candidates, name):
    candidates_with_name = []
    for candidate in candidates:
        if name.lower() in candidate["name"].lower():
            candidates_with_name.append(candidate)
    return candidates_with_name
