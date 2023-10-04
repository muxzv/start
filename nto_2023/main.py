from flask import Flask, request, jsonify, make_response
import requests
import random

app = Flask(__name__)
# настройка поддержки кириллицы
app.config['JSON_AS_ASCII'] = False

# маршрут по умолчанию
@app.route('/')
def index():
	return 'Hello from Flask!'

def get_film(genre):
	# список фильмов по жанру
	films = requests.get(f'https://yupest2.pythonanywhere.com/api/v1.0/movies/?genre={genre}').json()['records']

	# случайный фильм в диапазоне от нулевого до последнего из списка
	film = films[random.randint(0, len(films)-1)]

	# строка ответа бота с рекомендацией фильма
	return '{} в жанре {}, сделан в стране: {} с рейтингом: {}'.format(film['Название'], film['Жанр'], film['Страна'], film['Средняя оценка'])

def get_result():
	# извлечение параметра
	req = request.get_json(force=True)
	result = req.get("queryResult")
	parameters = result.get("parameters")
	# название параметра в соответствии с названием параметра сущности в интенте Genres
	# здесь можно задать переменные для каждого параметра, если их несколько
	genre = parameters.get("genre")

	# если параметр задан, вернем случайный фильм
	if genre:
		return {'fulfillmentText': get_film(genre)}

# маршрут webhook
@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	return make_response(jsonify(get_result()))

app.run(host='0.0.0.0', port=5000)