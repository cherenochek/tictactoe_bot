import telebot

bot = telebot.TeleBot('5624995439:AAGt6cHlf3gwB_ef40nH99eZc74pbTKFryw')

@bot.message_handlers(commands=['start'])
def start(message):
    bot.send