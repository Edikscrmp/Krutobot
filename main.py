import telebot
import random
bot = telebot.TeleBot("hash")

list=["Круто!", "Превосходно!","Восхитительно!","Хайпово","Супер!","Прелестно!"]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "Цена на товар снижена:" in message.text:
        bot.send_message(message.chat.id, "Ого")
        bot.send_message(message.chat.id, list[random.randint(0, 5)])

bot.polling(none_stop=True, interval=0)
