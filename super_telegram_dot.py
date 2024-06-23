import sqlite3
import telebot
import os, sys

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DB_PATH = os.getenv('DB_PATH')

bot = telebot.TeleBot(API_TOKEN)


def get_vacancies(username):
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        sql_query = """
            SELECT v.* 
            FROM learning_app_vacancy AS v
            JOIN accounts_dearuser AS u ON v.owner_id = u.id
            WHERE u.username = ?
        """
        cursor.execute(sql_query, (username,))
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()


# Команда start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Пожалуйста, введите ваше имя пользователя:")


# Обработка сообщений с именем пользователя
@bot.message_handler(func=lambda message: True)
def handle_username(message):
    username = message.text
    bot.reply_to(message, f"Спасибо, {username}! Сейчас найду ваши вакансии...")
    vacancies = get_vacancies(username)
    if isinstance(vacancies, str):
        bot.send_message(message.chat.id, f"Произошла ошибка: {vacancies}")
    elif vacancies:
        for vacancy in vacancies[:10]:
            for value in vacancy[1:4]:
                if value is not None:
                    bot.send_message(message.chat.id, value)
    else:
        bot.send_message(message.chat.id, "У вас нет вакансий.")


# Запуск бота
bot.polling()
