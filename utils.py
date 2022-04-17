import json


def get_info():
    with open("candidates.json", "r", encoding="utf-8") as f:
        info = json.load(f)
    return info


def get_candidates_list(info):
    line = []
    for candidate in info:
        line.append(candidate['name'])
        line.append(candidate['position'])
        line.append((candidate['skills']).lower() + "\n")
    formate_list = "\n".join(line)
    return formate_list


def get_candidate_info(info, x):
    for candidate in info:
        if x == int(candidate["id"]):
            return candidate
    return None


def get_candidate_skills(info, x):
    candidate_list = []
    for candidate in info:
        if x.lower() in candidate["skills"].lower():
            candidate_list.append(candidate)
    return candidate_list
