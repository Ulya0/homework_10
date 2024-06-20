import json


def load_candidates():
    """Загружает данные из файла"""

    with open('candidates.json', 'r') as file:
        candidates_json = json.load(file)
        return candidates_json


def get_all():
    """Выводит список всех кандадатов"""

    candidates = load_candidates()
    list_candidates = []
    for line in candidates:
        candidate = f"{line['name']} - {line['position']}, {line['skills']}"
        list_candidates.append(candidate)
    return ', '.join(list_candidates)


def get_by_pk(pk):
    """Выводит кандидата по pk"""

    candidates = load_candidates()
    for candidate in candidates:
        if pk == candidate['pk']:
            picture = candidate['picture']
            candidate = f"{candidate['name']} - {candidate['position']}, {candidate['skills']}"
            return picture, candidate


def get_by_skill(skill_name):
    """Выводит список кандидатов по навыку"""

    candidates = load_candidates()
    list_candidates_by_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            candidate = f"{candidate['name']} - {candidate['position']}, {candidate['skills']}"
            list_candidates_by_skill.append(candidate)
    return ', '.join(list_candidates_by_skill)
