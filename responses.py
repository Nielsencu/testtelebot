
def welcome_text(user_firstname):
    return f'<b>Hello, {user_firstname}!</b>\n\n' + f'Rating is now open for (Breakfast/Dinner), navigate to respective menu items to rate!'

def menu_text():
    return f'Click to see items and rate!'

def menuItem_text(menuItem):
    return f'{menuItem} Menu Items\n\n' + f"Today's rating for {menuItem} is (rating)"

def cumulativeRating_text():
    return f"Here are the cumulative ratings of the menus this week"