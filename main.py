import telebot
from telebot import types
import composer_table
from composer_table import *

import time

bot = telebot.TeleBot('6316626333:AAEyLAeyYKQzsvqSl7ggLYOQ1zSaou_K6hA');

@bot.message_handler(commands=['start'])
def handle_start(message):
    hello_text = "☀️Добрый день!  ☀️\n\nЯ помогаю следить за рекламацией в компании <b>Bazis Telecom</b>!\n\nМне понятны только команды, а также я реагирую на нажатие кнопок.\n\nНапишите /help для вывода более подробной информации о командах."
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, hello_text, parse_mode="html",reply_markup=remove_keyboard)

@bot.message_handler(commands=['help'])
def handle_start(message):
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "<b>Вам доступны следующие команды:</b>\n\n 👤 /getinfo - Показать информацию о клиенте\n 🆘 /support - Нашли ошибку? Сообщите, пожалуйста, поддержке!", parse_mode="html", reply_markup=remove_keyboard)

@bot.message_handler(commands=['support'])
def handle_start(message):
    bot.send_message(message.from_user.id, "Если вы обнаружили ошибку в работе бота, напишите @Barbarian_dm. Так же можете предлагать свои варианты по улучшению функционала!")

@bot.message_handler(commands=['getinfo'])
def handle_start(message):

    clients = composer_table.get_clients()
    string = "<b>📌Имена клиентов:📌</b> \n\n"
    number = 1
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    for i in range(0, len(clients), 1):
        unit = f"{number}. <a href='/command_help'>{clients[i]}</a> \n\n"
        string += unit
        keyboard.add(types.KeyboardButton(f"{clients[i]}"))
        number += 1
        
    bot.send_message(message.from_user.id, string + "Для вывода <b>подробной информации</b> по рекламации клиента <b>нажмите на кнопку с соответсвующим именем</b>.", parse_mode="html", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_input)

def handle_input(message):

    chat_id = message.chat.id

    if not(message.text.startswith('/')):
        input = f"⏳Получение информации о клиенте <b>{message.text}</b>... \n"
        message_while = bot.send_message(message.from_user.id, input, parse_mode="html").message_id

        smile = ["👤", "","","","📝","📅","","","","","","","","","","","","","","","",""]
        stringuxa = ""

        data = composer_table.get_info(str(message.text))

        for i in range(0, len(data[0]), 1):
            if not(data[1][i] == ''):
                unit = f"<b>✅ {data[0][i]}: </b> <i>{data[1][i]}</i>\n\n"
                stringuxa += unit
            else:
                unit = f"<b>❗{data[0][i]}: </b> <i>не заполнено</i>\n\n"
                stringuxa += unit

        # keyboard = types.ReplyKeyboardMarkup(row_width=1)
        # keyboard.row()
        # btn1 = types.KeyboardButton("/getclients")
        # btn2 = types.KeyboardButton("/help")
        # keyboard.add(btn1, btn2)

        bot.send_message(message.from_user.id, stringuxa, parse_mode="html")
        bot.delete_message(chat_id, message_while)
        bot.register_next_step_handler(message, handle_input)
    else:
        bot.send_message(message.from_user.id, "⛔ Упс! Клиента с таким именем не найдено. Выполните команду /getinfo ещё раз или просмотрите список всех команд с помощью /help.", parse_mode="html")






bot.polling(none_stop=True, interval=0)