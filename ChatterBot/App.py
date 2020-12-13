from chatterbot import ChatBot
from chatterbot.response_selection import get_first_response, get_random_response
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request
from chatterbot.response_selection import get_most_frequent_response
from datetime import date
import json
import time

from .modules.repair import get_repair_response
from .modules.laptopAdvisory import get_laptop_response
from .modules.accessories_advisory import accessories

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
				 #response_selection_method=get_first_response,
				 read_only=True)
trainer = ChatterBotCorpusTrainer(my_bot)

my_bot.storage.drop()
trainer.train('G:\Desktop\Document20201\AI\ChatterBot17\ChatterBot\Warranty.yml')
trainer.train("G:\Desktop\Document20201\AI\ChatterBot17\ChatterBot\laptop.yml")

@app.route("/")
def home():
	return render_template("index.html")


## Tư vấn bán hàng
@app.route("/get/advisory")
def get_response():
    userText = request.args.get('msg')
    if get_laptop_response(my_bot, request):
        return get_laptop_response(my_bot, request)
    elif accessories(my_bot, userText.lower()):
        return accessories(my_bot, userText.lower())


## Thông tin bảo hành
@app.route("/get/repair")
def get_repair():
	return get_repair_response(my_bot, request)


if __name__ == "__main__":
    app.run()
