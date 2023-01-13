from flask import Flask, render_template
from utils import *
# создаем приложение
app = Flask(__name__, template_folder='templates')


# вьюшка (ссылка) главной страницы
@app.route('/')
def page_index():
    candy = load_candidates_from_json()
    return render_template('list.html', candy=candy)


# вьюшка страницы при поиске по id
@app.route('/candidate/<int:x>')
def show_candidates(x):
    cand = get_candidate(x)
    return render_template('single.html', cand=cand)


# вьюшка страницы при поиске по name
@app.route('/search/<candidate_name>')
def cand_by_name(candidate_name):
    can = get_candidates_by_name(candidate_name)
    return render_template('search.html', can=can)


# вьюшка страницы при поиске по skill
@app.route('/skill/<skill_name>')
def c_by_skill(skill_name):
    c = get_candidates_by_skill(skill_name)
    return render_template('skill.html', c=c)


# запуск приложения
app.run()