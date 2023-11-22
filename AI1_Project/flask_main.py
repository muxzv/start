# AI1

import requests
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
# настройка поддержки кириллицы
app.config['JSON_AS_ASCII'] = False

# маршрут по умолчанию
@app.route('/')
def index():
  return 'Hello from AI1!'

@app.route('/max_get_json')
def json_example():
    return 'JSON Max Object'

def get_fio_output1(session, fio):
  text = f'Я узнал Вас, {fio}! Что хотите спросить?'
  outputContextName = session + "/contexts/contact"
  contactValue = fio

  return {
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            text
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": outputContextName,
        "lifespanCount": 50,
        "parameters": {
          "email": contactValue
        }
      }
    ]
  }

def get_fio(session, contact):
  headers={'User-Agent': 'Chrome'}

  rs = requests.get("https://cosmbrand.com/dialogflow_entry.ashx?action=catch&contact="+contact, headers=headers)
  rs_obj = rs.json()

  fio = rs_obj.get('fio')

  if fio:
  # строка ответа бота
    return get_fio_output1(session, fio)
  else:
    return {'fulfillmentText': "Отлично! Что Вы хотели бы узнать?"}
    
def get_discount(contact):
  return contact

def get_result():
  # извлечение параметров
  req = request.get_json(force=True)
  #print(req)
  session = req.get("session")
  result = req.get("queryResult")
  parameters = result.get("parameters")
  intent = result.get("intent").get("displayName")
  phone = parameters.get("phone-number")
  email = parameters.get("email")
  contact = phone if phone else email

  if intent == "Phone":
    return get_fio(session, contact)
  elif intent == "Discount":
    print(req)
    return {'fulfillmentText': get_discount(contact)}
  else:
    return {'fulfillmentText': 'Не понимаю тебя'}

# маршрут webhook
@app.route('/webhook', methods = ['POST'])
def webhook():
    return make_response(jsonify(get_result()))

app.run(host='0.0.0.0', port=5000)
