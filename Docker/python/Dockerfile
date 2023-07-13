FROM python:3.8

RUN pip install --upgrade pip

RUN pip install gspread telebot mysql-connector-python

# Запускаем команду по умолчанию при старте контейнера
CMD ["python", "main.py"]