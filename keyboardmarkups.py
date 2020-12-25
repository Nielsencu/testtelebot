from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)


def start_options():
    button_list = [
        InlineKeyboardButton(text = "Breakfast Menu", callback_data = "menu.breakfast"),
        InlineKeyboardButton(text = "Dinner Menu", callback_data = "menu.dinner"),
        InlineKeyboardButton(text = "Help", callback_data = "start.help"),
        InlineKeyboardButton(text = "View cumulative ratings", callback_data = "start.ratings")
    ]
    colnum=2
    return InlineKeyboardMarkup(abstract_button(button_list,colnum))

def menu_options(timeofday):

    if timeofday == 'breakfast':
        button_list = [
            InlineKeyboardButton(text = "Self service", callback_data = "menuItem.selfservice"),
            InlineKeyboardButton(text = "Western", callback_data = "menuItem.western"),
            InlineKeyboardButton(text = "Dim Sum/Congee/Noodle", callback_data = "menuItem.noodle"),
            InlineKeyboardButton(text = "Asian", callback_data = "menuItem.asian"),
            InlineKeyboardButton(text = "Asian Vegetarian", callback_data = "menuItem.asianveg"),
            InlineKeyboardButton(text = "Malay", callback_data = "menuItem.malay"),
            InlineKeyboardButton(text = "Halal Vegetarian", callback_data = "menuItem.halalveg"),
            InlineKeyboardButton(text = "Grab & Go", callback_data = "menuItem.grabngo"),
        ]
    else:
        button_list = [
            InlineKeyboardButton(text = "Self service", callback_data = "menuItem.selfservice"),
            InlineKeyboardButton(text = "Western", callback_data = "menuItem.western"),
            InlineKeyboardButton(text = "Noodle", callback_data = "menuItem.noodle"),
            InlineKeyboardButton(text = "Asian", callback_data = "menuItem.asian"),
            InlineKeyboardButton(text = "Vegetarian", callback_data = "menuItem.veg"),
            InlineKeyboardButton(text = "Malay", callback_data = "menuItem.malay"),
            InlineKeyboardButton(text = "Indian", callback_data = "menuItem.indian"),
        ]
    
    back_button = InlineKeyboardButton(text = "Back", callback_data = "start.home")
    return InlineKeyboardMarkup(abstract_button(button_list,colnum = 2, footer = [back_button]))

def menuItem_options(menuItem):
    if menuItem:
        placeholder = "Replace photo"
        colnum=2
    else:                  
        placeholder = "Attach photo"
        colnum=1
    button_list = [
        InlineKeyboardButton(text = placeholder, callback_data = "menuItem.western.attach"),
        InlineKeyboardButton(text = "Rate", callback_data = "menuItem.western.rate"),
    ]     

    back_button = InlineKeyboardButton(text = "Back", callback_data = "start.home")
    return InlineKeyboardMarkup(abstract_button(button_list,colnum, footer = [back_button]))

def abstract_button(button_list,colnum, footer = None, header = None):


    buttons = [button_list[i:i+colnum] for i in range(0, len(button_list),colnum)]

    if header:
        buttons.insert(0, header)
    if footer:
        buttons.append(footer)

    return buttons