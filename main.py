import os
from flask import Flask, request
import telebot

app = Flask(__name__)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@app.route('/')
def index():
    return 'Listen to always awesome news here: http://websdr.ewi.utwente.nl:8901/ !'


@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True), bot)
    bot.process_new_updates([update])
    return 'OK'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Sorry: Your Princess Is in The Another Castle!')


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)


def main():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://python-bot-test1.herokuapp.com/{BOT_TOKEN}")
    port = int(os.environ.get('PORT', 5000)) #set to 5000 if undefined
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()