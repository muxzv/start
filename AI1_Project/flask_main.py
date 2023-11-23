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

def get_fio_output1(session, client_id, fio):
  text = f'Я узнал Вас, {fio}! Что хотите спросить?'
  outputContextName = session + "/contexts/contact"

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
          "client_id": client_id
        }
      }
    ]
  }

def get_fio_output2(session, client_id):
  text = 'Отлично! Что Вы хотели бы узнать?'
  outputContextName = session + "/contexts/contact"
  
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
          "client_id": client_id
        }
      }
    ]
  }

def get_fio(session, contact):
  headers={'User-Agent': 'Chrome'}

  rs = requests.get("https://cosmbrand.com/dialogflow_entry.ashx?action=catch&contact="+contact, headers=headers)
  rs_obj = rs.json()

  fio = rs_obj.get('fio')
  client_id = rs_obj.get('client_id')
  isNewClient = rs_obj.get('is_new')
  
  if not isNewClient:
    return get_fio_output1(session, client_id, fio)
  else:
    return get_fio_output2(session, client_id) 
    
def get_discount(client_id):
  headers={'User-Agent': 'Chrome'}
  
  rs = requests.get("https://cosmbrand.com/dialogflow_entry.ashx?action=discount&client_id=" + client_id, headers=headers)
  rs_obj = rs.json()
  discount = rs_obj.get('discount')
  return  {'fulfillmentText': f'Ваша скидка: {discount}%.'}
  
def get_result():
  # извлечение параметров из запроса
  req = request.get_json(force=True)

  session = req.get("session")
  result = req.get("queryResult")
  parameters = result.get("parameters")
  intent = result.get("intent").get("displayName")
  
  if intent == "Phone":
    phone = parameters.get("phone-number")
    email = parameters.get("email")
    contact = phone if phone and len(phone)>5 else email
    return get_fio(session, contact)
  elif intent == "Discount":
    client_id = req['queryResult']['outputContexts'][0]['parameters']['client_id']
    return get_discount(client_id)
  else:
    return {'fulfillmentText': 'Не понимаю тебя'}

# маршрут webhook
@app.route('/webhook', methods = ['POST'])
def webhook():
    return make_response(jsonify(get_result()))

app.run(host='0.0.0.0', port=5000)
