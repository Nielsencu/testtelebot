from responses import (welcome_text, menu_text, menuItem_text)
from telegram import ParseMode
from keyboardmarkups import (menu_options, menuItem_options, start_options)

MAIN = range(0)

def handle_home(update,context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= welcome_text(update.effective_chat.first_name),
        reply_markup = start_options(),
        parse_mode = ParseMode.HTML
    )
    return MAIN


def handle_help(update,context):
    return MAIN

def handle_cumulativerating(update,context):
    return MAIN

def handle_menu(timeofday):

    def send_message(update,context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= menu_text(),
            reply_markup = menu_options(timeofday = timeofday),
            parse_mode = ParseMode.HTML
        )
        return MAIN
    return send_message

def handle_menu_item(menuItem):

    def send_message(update,context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= menuItem_text(menuItem = menuItem),
            reply_markup = menuItem_options(menuItem = menuItem),
            parse_mode = ParseMode.HTML
        )
        return MAIN
    return send_message

