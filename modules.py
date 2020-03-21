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


def deleteMessage(bot,query):
    message = query.message.message_id
    chat = query.message.chat.id
    bot.delete_message(chat,message)
