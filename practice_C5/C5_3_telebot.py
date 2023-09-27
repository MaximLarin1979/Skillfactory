import telebot

bot = telebot.TeleBot("6699749162:AAG7JJL7G4aSvpuPEEHagLZxjdYMdbsANMs")


@bot.message_handler(content_types=['text', ])
def reply_message(message: telebot.types.Message):
    bot.reply_to(message, f'привет, {message.chat.username} , "{message.text}" - '
                          f'эту твою фразу я понимаю, но могу ответить пока только агу агу :)')

@bot.message_handler(content_types=['photo', ])
def reply_photo(message: telebot.types.Message):
    bot.reply_to(message, f'привет, {message.chat.username} , красивая картинка агу агу :)')


bot.polling(none_stop=True)
