import telebot
from telebot import types
import src.python.composer_table as composer_table
from src.python.composer_table import *

import time

# Основной бот
# bot = telebot.TeleBot('6316626333:AAEyLAeyYKQzsvqSl7ggLYOQ1zSaou_K6hA');

# Резервный бот
bot = telebot.TeleBot('5932725163:AAG0JIVZ86rq70k2mSjcx2Yg810J0oYKNfE');

@bot.message_handler(commands=['start', 'help', 'support', 'getinfo', 'tips'])
def handle_output(message):
    if message.text == "/start":
        hello_text = "☀️Добрый день!☀️\n\nЯ помогаю следить за рекламацией в компании <b>Bazis Telecom</b>!\n\nМне понятны только команды, а также я реагирую на нажатие кнопок.\n\nНажмите на 👉 /help для вывода более подробной информации о командах."
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, hello_text, parse_mode="html", reply_markup=remove_keyboard)
    elif message.text == "/help":
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "<b>Вам доступны следующие команды:</b>\n\n 👤 /getinfo - Показать информацию о клиенте\n 👽 /tips - Полезные советы по пользованию ботом\n 🆘 /support - Нашли ошибку? Сообщите, пожалуйста, поддержке!", parse_mode="html", reply_markup=remove_keyboard)
    elif message.text == "/support":
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Если вы обнаружили ошибку в работе бота, напишите @Barbarian_dm. Так же можете предлагать свои варианты по улучшению функционала!", reply_markup=remove_keyboard)
    elif message.text == "/getinfo":
        clients = composer_table.get_clients()
        string = "<b>📌Имена клиентов:📌</b> \n\n"
        number = 1
        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        for i in range(0, len(clients), 1):
            unit = f"{number}. <a href='/command_help'>{clients[i]}</a> \n\n"
            string += unit
            keyboard.add(types.KeyboardButton(f"{clients[i]}"))
            number += 1

        bot.send_message(message.from_user.id,
                         string + "Для вывода <b>подробной информации</b> по рекламации клиента <b>нажмите на кнопку с соответсвующим именем 👇</b>",
                         parse_mode="html", reply_markup=keyboard)
        bot.register_next_step_handler(message, handle_input)
    elif message.text == "/tips":
        tips = "💥<b>Полезные советы</b>💥\n\n1. Вместо того чтобы вписывать команды самостоятельно, вы можете нажать на интересующую команду, если увидите её в тексте. Она выполнится автоматически.\n2. Вы можете выбирать команды в <b>меню</b>, а также нажимать на появляющиеся под клавиатурой кнопки для выбора каких-либо дополнительных параметров в зависимости от команды.\n\n⏳ Количество полезных советов скоро вырастет :)"
        bot.send_message(message.from_user.id, tips, parse_mode='html')

def handle_input(message):

    chat_id = message.chat.id

    if composer_table.find_client(message.text):
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

        bot.send_message(message.from_user.id, stringuxa, parse_mode="html")
        bot.delete_message(chat_id, message_while)
        bot.register_next_step_handler(message, handle_input)
    elif message.text.startswith('/'):
        handle_output(message)
    else:
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, f"⛔ Упс! Клиента с таким именем не найдено. Выполните команду /getinfo ещё раз и нажмите на кнопку с интересующим клиентом.", parse_mode="html", reply_markup=remove_keyboard)
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     remove_keyboard = types.ReplyKeyboardRemove()
#     bot.send_message(message.from_user.id, "⚠ Мне понятны только команды, а также я реагирую на нажатие кнопок.\n\nНажмите на 👉 /help для вывода более подробной информации о командах.", reply_markup=remove_keyboard)




bot.polling(none_stop=True, interval=0)