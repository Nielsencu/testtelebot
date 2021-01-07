from responses import (welcome_text, menu_text, menuItem_text, help_text)
from telegram import ParseMode
from keyboardmarkups import (menu_options, menuItem_options, start_options, rating_options, back_button_only)
from models import FoodSet
from config import SQL_SESSION
from datetime import datetime as dt

session = SQL_SESSION

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
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = help_text(),
        reply_markup = back_button_only(),
        parse_mode = ParseMode.HTML
    )
    return MAIN

def handle_seeall(update,context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text="Western:\nMac and Cheese\nMarble baked Potato\nChicken Chop\n\nAsian:\n...\n..."
    )
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
        menu = session.query(FoodSet).filter(FoodSet.settype == menuItem).first()
        if menu is None:
            rating = 'Menu not found'
        else:
            try:
                rating = round(menu.rating/ menu.total_rater,2)
            except ZeroDivisionError:
                rating = 'null'

        now = dt.now()
        date_time = now.strftime("%Y%m%d")
        if menu is not None:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text= menuItem_text(menuItem = menuItem, rating = rating, user_have_rated = date_time == menu.last_rated_at, number_people_rated = menu.total_rater, foodItems=['Mac and cheese', 'Marble baked Potato', 'Chicken Chop']),
                reply_markup = menuItem_options(menuItem = menuItem),
                parse_mode = ParseMode.HTML
            )
        else:
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text="Not found"
                )
        return MAIN
    return send_message

def handle_rating_number(menuItem):
    def ask_to_rate(update,context):
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Please rate from 1-5",
            reply_markup = rating_options(menuItem),
            )
        return MAIN
    return ask_to_rate

def handle_rating(menuItem,rating):
    
    def update_rating(update,context):
        now = dt.now()  # Rate only once a day
        date_time = now.strftime("%Y%m%d")
        menu = session.query(FoodSet).filter(FoodSet.settype == menuItem).first()
        if not(date_time == menu.last_rated_at):
            session.query(FoodSet).filter(FoodSet.settype == menuItem).update({"rating": FoodSet.rating + rating, "last_rated_at": date_time, "total_rater": FoodSet.total_rater + 1})
            session.commit()
        else:
            context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "You have rated already!",
            )
        return handle_menu_item(menuItem=menuItem)(update,context)
    return update_rating

def handle_rated_already(update,context):

    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "You have rated already!"
    )

    return MAIN



