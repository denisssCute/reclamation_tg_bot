# Telegram Bot For Reclamation

Данный бот является собственностью компании <a href="https://bztel.ru/">«OOO Базис Телеком»</a> и разработан для автоматизации и облегчения контроля за рекламацией.

<h4>Актуальная версия бота: reclamation_tg_bot Beta</h4>

Принцип действия бота:
1. В качестве БД используется таблица Google Table, содержащая 21 столбец, в которые заносятся данные о каждой рекламации.
2. Бот взаимодействует с Google Table с помощью <a href="https://dvsemenov.ru/google-tablicy-i-python-podrobnoe-rukovodstvo-s-primerami/#__Google_Api_Console">Google Api Console</a>
3. Файл composer_table.py содержит в себе функции для обработки данных из Google Table.
4. Файл main.py содержит в себе функционал бота и обращается к composer_table.py для получения данных при запросе пользователя.