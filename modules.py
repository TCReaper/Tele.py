from telebot import types


#   import file for modules


def createIKM(array_of_options):
    data = array_of_options
    markup = types.InlineKeyboardMarkup()
    for element in data:
        button = types.InlineKeyboardButton(element,callback_data=element)
        markup.add(button)
    return markup


def createRKM(array_of_options):
    data = array_of_options
    markup = types.ReplyKeyboardMarkup(row_width=3,one_time_keyboard=True)
    for element in data:
        button = types.KeyboardButton(element)
        markup.add(button)
    return markup


def editMessage(bot,query,text='',markup=None):
    message = query.message.message_id
    chat = query.message.chat.id
    
    if markup == 'None':
        bot.edit_message_text(message_id=message,
                                  chat_id=chat,
                                  text=text)
        return True
    
    else:
        bot.edit_message_text(message_id=message,
                              chat_id=chat,
                              text=text,
                              reply_markup=markup)
        return True


def deleteQuery(bot,query):
    message = query.message.message_id
    chat = query.message.chat.id
    bot.delete_message(chat,message)

def deleteMessage(bot,message):
    msg = message.message_id
    chat = message.chat.id
    bot.delete_message(chat,msg)

def createPTBoard(date):
    
    cross = u'\U0001F17E'
    tick = u'\U00002705'

    board = [date,[cross,'  ad'],[cross,'  hs' ],[cross,'  ja' ],[cross,'  jo' ]]

    return board

def printPTBoard(board,bot,id):

    date = board[0]
    board = board[1:]
    sentence = str(date)+'\n'
    for i in board:
        sentence += i[0] + i[1] + '\n'
    message = bot.send_message(id, sentence,reply_markup=createIKM(['edit']))

    return message
    
    
    
    

    
