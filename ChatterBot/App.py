import json

from chatterbot import ChatBot
from chatterbot.response_selection import get_first_response, get_random_response, get_most_frequent_response
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

my_bot = ChatBot("MyChatterBot", storage_adapter='chatterbot.storage.SQLStorageAdapter',
                 logic_adapters=[
                     {
                         'import_path': 'chatterbot.logic.BestMatch',
                         'default_response': 'Mình chưa hiểu rõ lắm, bạn vui lòng nhắc lại được không ạ'
                     }
                 ],
                 response_selection_method=get_random_response,
                 read_only=True)
trainer = ChatterBotCorpusTrainer(my_bot)

my_bot.storage.drop()
trainer.train("accessories")


def accessories_link(type, model):
    file = open('data/accessories.json')
    data = json.load(file)
    if model == 'common':
        response = str(my_bot.get_response('loại_phụ_kiện'))
    else:
        response = str(my_bot.get_response('hãng_phụ_kiện'))
    response = response.replace('!type!', type.upper())
    link = '<a href="' + data[type][
        model] + '" target="_blank">' + type.upper() + ('' if model == 'common' else ' ' + model.upper()) + '</a>'
    response = response.replace('!link!', link)
    if '!model!' in response:
        response = response.replace('!model!', model.upper())
    print(response)
    return response


def accessories_analyze(accessories):
    file = open('data/accessories.json')
    data = json.load(file)
    model = 'common'
    if 'ram' in accessories:
        type = 'ram'
    elif 'ssd' in accessories:
        type = 'ssd'
    elif 'hdd' in accessories:
        type = 'hdd'
    elif 'vga' in accessories:
        type = 'vga'
    elif 'adapter' in accessories:
        type = 'adapter'
    elif 'cpu' in accessories:
        type = 'cpu'
    for e in data[type]:
        if e in accessories:
            model = e
            break
    return accessories_link(type, model)


def accessories(userText):
    msgAfterWait = ''
    miliseconds = 0
    output = my_bot.get_response('unknown')
    if 'ngu vcl' in userText:
        output = my_bot.get_response('ngu vcl')
    if 'phụ kiện' in userText:
        output = my_bot.get_response('phụ kiện')
    if 'ram' in userText or 'cpu' in userText \
            or 'sạc' in userText or 'ổ cứng' in userText \
            or 'hdd' in userText or 'ssd' in userText or 'vga' in userText:
        output = accessories_analyze(userText)
    return {"output": str(output), 'timeOut': {'msg': msgAfterWait, 'miliseconds': miliseconds}}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText = userText.lower()
    print(userText)
    output = accessories(userText)
    return output


if __name__ == "__main__":
    app.run()
