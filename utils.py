# импортируем библиотеку json
import json

# открываем json файл с помощью функции
def load_candidates_from_json():
    with open('/Users/miya/PycharmProjects/skypro 11.2/smth.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# функция, находящая кандидата по id
def get_candidate(candidate_id):
    for i in load_candidates_from_json():
        if i['id'] == candidate_id:
            return i


# функция, находящая кандидата по имени
def get_candidates_by_name(candidate_name):
    kandidats = []
    for i in load_candidates_from_json():
        if candidate_name.lower() in i['name'].lower():
            kandidats.append(i)
    return kandidats


# функция, находящая кандидата по скиллу
def get_candidates_by_skill(skill_name):
    kandido = []
    for i in load_candidates_from_json():
        i['skills'] = i['skills'].lower()
        skill_name = skill_name.lower()
        if skill_name in i['skills']:
            kandido.append(i)
    return kandido
