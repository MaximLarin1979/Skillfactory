import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

keys = {'доллар': 'USD', 'евро': 'EUR', 'рубль': 'RUB'}


@bot.message_handler(commands=['start', 'help'])
def bot_help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n' \
           '<имя переводимой валюты> <в какую валюту перевести> <количество переводимой валюты>\n' \
           'Чтобы увидеть список доступных валют, введите команду "/values"'
    bot.reply_to(message, text)


def bot_values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join(text, key, )
    bot.reply_to(message, text)
