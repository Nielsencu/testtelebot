from responses import (welcome_text, menu_text, menuItem_text)
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
    menu = session.query(FoodSet).filter(FoodSet.settype == menuItem).first()
    if menu == None:
        rating = 'Menu not found'
    else:
        try:
            rating = round(menu.rating/ menu.total_rater,2)
        except ZeroDivisionError:
            rating = 'No ratings yet'
    
    def send_message(update,context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= menuItem_text(menuItem = menuItem, rating = rating),
            reply_markup = menuItem_options(menuItem = menuItem),
            parse_mode = ParseMode.HTML
        )
        return MAIN
    return send_message

def handle_rating_number(update,context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Please rate from 1-5",
        reply_markup = rating_options(),
        )
    return MAIN

def handle_rating(menuItem,rating):
    
    def update_rating(update,context):
        menu = session.query(FoodSet).filter(FoodSet.settype == menuItem).first()

        session.query(FoodSet).filter(FoodSet.settype == menuItem).update({"rating": FoodSet.rating + rating, "total_rater": FoodSet.total_rater + 1})
        '''
        now = dt.now()
        date_time = now.strftime("%Y%m%d")
        if date_time == menu.last_rated_at:
            context.bot.send_message(chat_id= update.effective_chat.id, text="You have rated already!")
        else:
            session.query(FoodSet).filter(FoodSet.settype == menuItem).update({"rating": FoodSet.rating + rating, "last_rated_at": date_time, "total_rater": FoodSet.total_rater + 1})
        '''
            
        session.commit()
        return MAIN

    return update_rating


