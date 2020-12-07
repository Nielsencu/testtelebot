from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

from config import SQL_SESSION
session = SQL_SESSION

from models import *

MAIN = range(0)

def start(update, context):
    username = update.message.from_user.username
    fullname = update.message.from_user.full_name
    user_id = update.message.from_user.id
    
    user = User(tele_id=user_id, tele_handle=username, name=fullname)

    session.add(user)
    session.commit()

    update.message.reply_text("Bot Started")

    return MAIN

def ping(update, context):
    message = update.message.text
    ping_count = message.count('ping')
    
    for i in range(ping_count):
        update.message.reply_text("Pong")

    return MAIN

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            MAIN: [MessageHandler(Filters.regex("ping"), ping)],
        },

        fallbacks=[]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    print("Bot Started")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    print("Initializing...")
    main()
