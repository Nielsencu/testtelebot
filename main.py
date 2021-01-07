from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,
                          ConversationHandler)
from responses import (welcome_text)
from keyboardmarkups import start_options
from handlers import (handle_menu, handle_menu_item, handle_seeall, handle_home, handle_help, handle_cumulativerating, handle_rating,handle_rating_number)

from config import SQL_SESSION
session = SQL_SESSION

from models import FoodSet, User, FoodImage

from mockdata import data


MAIN = range(0)

def start(update, context):
    username = update.message.from_user.username
    fullname = update.message.from_user.full_name
    user_id = update.message.from_user.id
    
    user = User(tele_id=user_id, tele_handle=username, name=fullname)

    session.add(user)
    for datas in data:
        query = session.query(FoodSet).filter(FoodSet.settype == datas[1]).filter(FoodSet.breakfastbool == datas[2]).first()
        if query == None:
            session.add(datas[0])
    session.commit()

    update.message.reply_text("Bot Started") 
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= welcome_text(update.effective_chat.first_name),
            reply_markup = start_options(),
            parse_mode = ParseMode.HTML
    )

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
            MAIN: [],
        },

        fallbacks=[]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(handle_home, pattern='^start.home'))
    dp.add_handler(CallbackQueryHandler(handle_help, pattern='^start.help'))
    dp.add_handler(CallbackQueryHandler(handle_seeall, pattern='^start.seeall'))
    dp.add_handler(CallbackQueryHandler(handle_cumulativerating, pattern='^start.cumulativerating'))

    dp.add_handler(CallbackQueryHandler(handle_menu(timeofday = 'breakfast'), pattern='^menu.breakfast'))
    dp.add_handler(CallbackQueryHandler(handle_menu(timeofday = 'dinner'), pattern='^menu.dinner'))
    
    dp.add_handler(CallbackQueryHandler(handle_rating_number(menuItem = 'western'), pattern='^rate.western'))    
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'western',rating = 1), pattern='^westernrate.1'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'western',rating = 2), pattern='^westernrate.2'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'western',rating = 3), pattern='^westernrate.3'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'western',rating = 4), pattern='^westernrate.4'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'western',rating = 5), pattern='^westernrate.5'))

    dp.add_handler(CallbackQueryHandler(handle_rating_number(menuItem = 'selfservice'), pattern='^rate.selfservice'))    
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'selfservice',rating = 1), pattern='^selfservicerate.1'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'selfservice',rating = 2), pattern='^selfservicerate.2'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'selfservice',rating = 3), pattern='^selfservicerate.3'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'selfservice',rating = 4), pattern='^selfservicerate.4'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'selfservice',rating = 5), pattern='^selfservicerate.5'))

    dp.add_handler(CallbackQueryHandler(handle_rating_number(menuItem = 'noodle'), pattern='^rate.noodle'))    
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'noodle',rating = 1), pattern='^noodle.1'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'noodle',rating = 2), pattern='^noodle.2'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'noodle',rating = 3), pattern='^noodle.3'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'noodle',rating = 4), pattern='^noodle.4'))
    dp.add_handler(CallbackQueryHandler(handle_rating(menuItem = 'noodle',rating = 5), pattern='^noodle.5'))

    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'selfservice'), pattern='^menuItem.selfservice'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'western'), pattern='^menuItem.western'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'noodle'), pattern='^menuItem.noodle'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'asian'), pattern='^menuItem.asian'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'asianveg'), pattern='^menuItem.asianveg'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'malay'), pattern='^menuItem.malay'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'grabngo'), pattern='^menuItem.grabngo'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'vegetarian'), pattern='^menuItem.veg'))
    dp.add_handler(CallbackQueryHandler(handle_menu_item(menuItem = 'indian'), pattern='^menuItem.indian'))
    

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
