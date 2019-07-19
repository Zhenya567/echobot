import telebot

bot = telebot.TeleBot("689311965:AAHFB8MvCxQmf0ny0utYuz_eLMfG3Yx9els")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id,message.text)

bot.polling(none_stop = True)