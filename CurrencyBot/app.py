import telebot
from token_keys import TOKEN, keys
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def bot_help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n' \
           '<имя переводимой валюты> <в какую валюту перевести> <количество переводимой валюты>\n' \
           'Чтобы увидеть список доступных валют, введите команду "/values"'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def bot_values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    if len(values) > 3:
        raise APIException('Слишком много параметров')
    quote, base, amount = values
    result = CurrencyConverter.get_price(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {result}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
