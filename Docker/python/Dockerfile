FROM python:3.8

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

#COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install gspread telebot mysql-connector-python

EXPOSE 8080

CMD ["python", "main.py"]
