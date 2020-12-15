import json

from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request
# Mn sửa lại cú pháp import phù hợp
from ChatterBot17.ChatterBot.modules.accessories_advisory import accessories
from ChatterBot17.ChatterBot.modules.general import get_general_response
from ChatterBot17.ChatterBot.modules.laptopAdvisory import get_laptop_response
from ChatterBot17.ChatterBot.modules.order import proccessOrder
from ChatterBot17.ChatterBot.modules.repair import get_repair_response
from ChatterBot17.ChatterBot.modules.warranty import get_warranty_response

app = Flask(__name__)

my_bot = ChatBot("MyChatterBot",
                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                 logic_adapters=[
                     {
                         'import_path': 'chatterbot.logic.BestMatch',
                         'default_response': 'Mình chưa hiểu rõ lắm, bạn vui lòng nhắc lại được không ạ'
                     }
                 ],
                 response_selection_method=get_random_response,
                 # response_selection_method=get_first_response,
                 read_only=True)
trainer = ChatterBotCorpusTrainer(my_bot)

# my_bot.storage.drop()  # chỉ cần học một lần
# trainer.train('brain')  # nếu dữ liệu thay đổi cần drop dữ liệu cũ đi học lại

with open('data/learned/conversation.json', 'w', encoding='utf-8') as file:
    file.flush()
    file.write('{}')

with open('data/ReadUser.json', 'w', encoding='utf-8') as file:
    file.flush()
    file.write('{"laptop": "", "price": 0, "purpose": ""}')


def json_conversation_save(userText, output):
    with open('data/learned/conversation.json', 'r', encoding='utf-8') as file:
        old_data = json.load(file)
        file.close()
    with open('data/learned/conversation.json', 'w', encoding='utf-8') as file:
        data = {userText: output}
        old_data.update(data)
        json.dump(old_data, file, ensure_ascii=False, indent=2)
        file.close()


@app.route("/")
def home():
    return render_template("index.html")


# general
@app.route("/get/general")
def get_general():  # get_general được gọi khi chưa chọn mục tư vấn
    userText = request.args.get('msg')
    output = get_general_response(my_bot, userText.lower())
    if output:
        json_conversation_save(userText,
                               output['output'])  # lưu cuộc hội thoại, tương tự với get_advisory và get_repair
    else:
        output = {'output': str(my_bot.get_response('unknown')),
                  'timeOut': {'msg': '', 'milisecond': 0}}
    return output


## Tư vấn bán hàng
@app.route("/get/advisory")
def get_advisory():
    userText = request.args.get('msg')
    output = None
    if get_laptop_response(my_bot, request):
        output = get_laptop_response(my_bot, request)
    elif accessories(my_bot, userText.lower()):
        output = accessories(my_bot, userText.lower())
    elif get_general_response(my_bot, userText.lower()):
        output = get_general_response(my_bot, userText.lower())
    output = output if output else {'output': str(my_bot.get_response('unknown')),
                                    'timeOut': {'msg': '', 'milisecond': 0}}
    json_conversation_save(userText, output['output'])
    return output


## Thông tin bảo hành - sửa chữa
@app.route("/get/repair")
def get_repair():
    userText = request.args.get('msg')
    output = {'output': 'unknown',
              'timeOut': {'msg': '', 'milisecond': 0}}
    if get_repair_response(my_bot, request):
        output = get_repair_response(my_bot, request)
    if get_warranty_response(my_bot, request):
        output = get_warranty_response(my_bot, request)
    elif get_general_response(my_bot, userText.lower()):
        output = get_general_response(my_bot, userText.lower())
    output = output if output else {'output': str(my_bot.get_response('unknown')),
                                    'timeOut': {'msg': '', 'milisecond': 0}}
    json_conversation_save(userText, output['output'])
    return output


if __name__ == "__main__":
    app.run()
