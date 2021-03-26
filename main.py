import time
import telebot
import datetime
from telebot import types
from token_var import token
from modules import *



TOKEN = token()
bot = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object



#           /help

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "just figure it out")


#           /newday

@bot.message_handler(commands=['newday'])
def start_day(message):
    dt = datetime.datetime.now().date()
    
    day = str("{:0>2d}".format(dt.day))
    month = str("{:0>2d}".format(dt.month))
    year = str(dt.year)[2:]

    today = day+month+year

    sentence = "good morning!! today is "+today+".\ndon't forget your PT today :)"
    bot.send_message(message.chat.id, sentence)
    
    time.sleep(2)
    sentence = "creating a board for PT..."
    message = bot.send_message(message.chat.id, sentence)
    board = createPTBoard(today)
    deleteMessage(bot,message)
    printPTBoard(board,bot,message.chat.id)
    

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    reply = query.message.chat.id
    if data.startswith('cancel'):
        editMessage(bot,query,text='function cancelled.')
        time.sleep(3)
        deleteMessage(bot,query)
    elif data.startswith('edit'):
        message = bot.send_message(reply, "select one to edit!!",
                                   reply_markup=createIKM(['ad','hs','ja','jo']))
        






bot.polling()
