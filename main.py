import telebot
from telebot import types
import composer_table
from composer_table import *
bot = telebot.TeleBot('6316626333:AAEyLAeyYKQzsvqSl7ggLYOQ1zSaou_K6hA');

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Вам доступны следующие команды:\n 1. /getclients - Показать всех клиентов")
#     elif message.text == "/getclients":
#         clients = composer_table.get_clients()
#         string = "<b>Имена клиентов:</b> \n\n"
#         number = 1
#         for i in range(0, len(clients), 1):
#             unit = f"{number}. <a href='/command_help'>{clients[i]}</a> \n\n"
#             string += unit
#             number += 1
#         bot.send_message(message.from_user.id, string, parse_mode="html")
#     else:
#         bot.send_message(message.from_user.id, "Я понимаю только команды.\nНапишите /help для вывода справки.")

@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    help_button = types.KeyboardButton('/help')
    settings_button = types.KeyboardButton('/settings')
    keyboard.add(help_button, settings_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Это справочная информация")

@bot.message_handler(commands=['settings'])
def handle_settings(message):
    bot.send_message(message.chat.id, "Настройки")
bot.polling(none_stop=True, interval=0)