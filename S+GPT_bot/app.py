import os
import telebot
import openai
import logging
import time
from tokens import TOKEN_TELEBOT, TOKEN_OPENAI
from users import users

bot = telebot.TeleBot(TOKEN_TELEBOT)
openai.api_key = TOKEN_OPENAI

# логирование
log_dir = os.path.join(os.path.dirname(__file__), 'ChatGPT_Logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=os.path.join(log_dir, 'error.log'), level=logging.ERROR,
                    format='%(levelname)s: %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# Обработчик команд /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 'Привет!\nЯ ChatGPT 3.5 бот компании S+Консалтинг\U0001F916\nЗадай мне любой вопрос, и я постараюсь '
                 'на него ответить!')


# Функция генерации ответа используя OpenAI API
def generate_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    return completion.choices[0].message.content


# Обработчик сообщений
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    if message.from_user.username not in users:
        bot.send_message(message.chat.id, 'Вы не авторизованы в чат-боте')
    else:
        prompt = message.text
        response = generate_response(prompt)
        bot.send_message(chat_id=message.from_user.id, text=response)


# Запуск бота
print('S+ ChatGPT бот запущен')

while True:
    try:
        bot.polling(none_stop=True)
    except (telebot.apihelper.ApiException, ConnectionError) as e:
        logging.error(str(e))
        time.sleep(5)
        continue
