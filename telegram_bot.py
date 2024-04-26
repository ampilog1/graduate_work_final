import os, sys
import django
from django.conf import settings
import telebot


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "learning_try_1.settings"

django.setup()


from learning_app.models import Vacancy

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)
# os.environ["DJANGO_SETTINGS_MODULE"] = "learning_try_1.settings"
# User_all = DearUser.objects.values()

# for vacancy_prep in vacancy_all[:20]:
#     vacancy_send = str([value for value in vacancy_prep.values() if value is not None])


# print(User_all)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello!Input your username")
    bot.send_message(message.chat.id, "Please")
    bot.send_message(message.chat.id, "Mister Anderson")



@bot.message_handler(func=lambda message: True)
def first_vacancy_20(message):
    chat_id = message.chat.id
    user_name = message.text
    vacancy_all = Vacancy.objects.filter(owner__username=user_name).values('name', 'link', 'address', 'salary')
    for element in vacancy_all[:20]:
        for value in element.values():
            if value is not None:
                bot.send_message(chat_id, value)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()