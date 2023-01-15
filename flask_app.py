from flask import Flask
from flask import request
import base64
from urllib.parse import urlparse
import http.client
import json
from telegram_library import MessageToTelegram
import traceback

from Marks_library import ready_s
from max_library import random_bot
import game_rocks_bot

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "OK"

@app.route("/9DB6594F-328E-4076-92EB-44BAC0F9BA5B/", methods=['GET'])
def hello_live():
    return "live"

@app.route("/9DB6594F-328E-4076-92EB-44BAC0F9BA5B/<s>", methods=['GET'])
def handle_get(s):
    #s1 = "d3d3LnB5dGhvbi5vcmc="
    b = s.encode("UTF-8")
    d = base64.b64decode(b)
    uri = d.decode("UTF-8")

    o = urlparse(uri)

    conn = http.client.HTTPSConnection("proxy.server:3128")
    conn.set_tunnel(o.hostname)
    conn.request("GET", o.path)
    r1 = conn.getresponse()
    #print(r1.status, r1.reason)
    data = r1.read()
    conn.close()

    return data

#@app.route("/9DB6594F-328E-4076-92EB-44BAC0F9BA5B/<s>", methods=['POST'])
@app.route("/9DB6594F-328E-4076-92EB-44BAC0F9BA5B", methods=['POST'])
def handle_post():
    #b = s.encode("UTF-8")
    #d = base64.b64decode(b)
    #uri = d.decode("UTF-8")
    #o = urlparse(uri)

    request.get_data()
    body=request.data

    #conn = http.client.HTTPSConnection("proxy.server:3128")
    #conn.set_tunnel(o.hostname)
    #headers = {"Content-Type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
    #conn.request("POST", o.path, body, headers)
    #response = conn.getresponse()
    #data = response.read()
    #conn.close()

    jss = json.loads(body)

    # jss["context"]

    bot_name = jss["bot"]
    in_s = jss["text"]
    context = jss["context"]

    try:
        if isinstance(context, str):
            context = json.loads(context)

        if bot_name == "HowManyMarks_bot":
            data = ready_s(in_s)
        elif bot_name == "muxzv_bot":
            data = random_bot(in_s)
        elif bot_name == "boxing_tbot":
            data = game_rocks_bot.Go(in_s, context)
        else:
            data = "Unknown bot"
    except Exception:
        data = traceback.format_exc()

    if isinstance(data, MessageToTelegram):
        out_dict = {'text': data.message, 'buttons': data.buttons}
        pass
    elif isinstance(data, tuple):
        out_dict = {'text': data[0], 'context': json.dumps(data[1])}
    else:
        out_dict = {'text': data}

    return json.dumps(out_dict)

if __name__ == "__main__":
    app.run()
