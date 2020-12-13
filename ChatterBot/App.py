import json

from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
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
with open('data/conversation.json', 'w', encoding='utf-8') as file:
    file.flush()
    file.write('{}')


def json_conversation_save(userText, output):
    with open('data/conversation.json', 'r', encoding='utf-8') as file:
        old_data = json.load(file)
        file.close()
    with open('data/conversation.json', 'w', encoding='utf-8') as file:
        data = {userText: output}
        old_data.update(data)
        json.dump(old_data, file, ensure_ascii=False, indent=2)
        file.close()


def accessories_link(type, model):
    file = open('data/accessories.json')
    data = json.load(file)
    file.close()
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
    if '!list' in response:
        list = str(data[type].keys()).replace("'", '')
        list = list.replace('dict_keys', '')
        list = list.replace('(', '')
        list = list.replace(')', '')
        list = list.replace('[', '')
        list = list.replace(']', '')
        list = list.replace('common,', '')
        response = response.replace('!list!', list.upper())
    print(response)
    return response


def accessories_analyze(userText):
    file = open('data/accessories.json')
    data = json.load(file)
    file.close()
    model = 'common'
    if 'ram' in userText:
        type = 'ram'
    elif 'ssd' in userText:
        type = 'ssd'
    elif 'hdd' in userText:
        type = 'hdd'
    elif 'vga' in userText:
        type = 'vga'
    elif 'sạc' in userText or 'adapter' in userText:
        type = 'adapter'
    elif 'ổ cứng' in userText:
        type = 'hdd'
    elif 'cpu' in userText:
        type = 'cpu'
    for e in data[type]:
        if e in userText:
            model = e
            break
    json_conversation_save(userText, type + ' ' + model)
    return accessories_link(type, model)

#route here
def get_accessories_response():
    userText = request.args.get('msg')
    userText = userText.lower()
    print(userText)
    msgAfterWait = ''
    miliseconds = 0
    output = None
    if 'ngu vcl' in userText:
        output = my_bot.get_response('ngu vcl')
    if 'phụ kiện' in userText:
        output = my_bot.get_response('phụ_kiện')
    if 'ram' in userText or 'cpu' in userText \
            or 'sạc' in userText or 'ổ cứng' in userText \
            or 'hdd' in userText or 'ssd' in userText or 'vga' in userText:
        output = accessories_analyze(userText)
    return {"output": str(output), 'timeOut': {'msg': msgAfterWait, 'miliseconds': miliseconds}} if output \
        else None


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
