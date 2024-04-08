import logging
from tkn import token
from telegram import Update
from datetime import datetime
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    questions = ["Yes","No"]
    message = await context.bot.send_poll(
        update.effective_chat.id,
        "AG Time for "+datetime.now().strftime("%a, %d %b"),
        questions,
        is_anonymous=False,
        allows_multiple_answers=False,
    )
    # Save some info about the poll the bot_data for later use in receive_poll_answer
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    context.bot_data.update(payload)

if __name__ == '__main__':
    application = ApplicationBuilder().token(token()).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("poll", poll))
    
    application.run_polling()