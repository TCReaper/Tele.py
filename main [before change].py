import time
import telebot
from token_var import token
from modules import *



TOKEN = token()
bot = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object



#           /help

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "try /start for more!!")



#           reply markup keyboard

@bot.message_handler(commands=['keyboard'])
def keyboard(message):
    markup = createRKM(['ECKSDEE','genius!','hehe xd','¯\_(ツ)_/¯'])
    bot.send_message(message.chat.id, "chat!!", reply_markup=markup)


#           /start

@bot.message_handler(commands=['start'])
def start_programme(message):

    markup = createIKM(['begin','cancel'])
    bot.send_message(message.chat.id, "option:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    reply = query.message.chat.id
    if data.startswith('cancel'):
        editMessage(bot,query,text='function cancelled.')
        time.sleep(3)
        deleteMessage(bot,query)
    elif data.startswith('begin'):
        markup = createIKM(['BOOM'])
        bot.send_message(reply, "dee dee dee", reply_markup=markup)
        deleteMessage(bot,query)
    elif data.startswith('BOOM'):
        editMessage(bot,query,text=u'\U0001F4A5')
        






bot.polling()
