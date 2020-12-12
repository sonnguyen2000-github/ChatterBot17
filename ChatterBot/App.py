from chatterbot import ChatBot
from chatterbot.response_selection import get_first_response
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
                 response_selection_method=get_first_response,
                 read_only=True)
trainer = ChatterBotCorpusTrainer(my_bot)

my_bot.storage.drop()
trainer.train("pcshop")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    output = str.lower(userText).split(' ')
    print(output)
    if 'xin chào' in userText:
        output = 'xin chào'
    return str(my_bot.get_response(str(output)))


if __name__ == "__main__":
    app.run()
