
def welcome_text(user_firstname):
    return f'<b>Hello, {user_firstname}!</b>\n\n' + f'Rating is now open for (Breakfast/Dinner), navigate to respective menu items to rate!'

def menu_text():
    return f'Click to see items and rate!'

def menuItem_text(menuItem, foodItems, rating, user_have_rated, number_people_rated):
    addedText=''
    for item in foodItems:
        addedText += item + '\n'
    if user_have_rated:
        addedText += '\nYou have rated this menu!'
    else:
        addedText += '\nYou have not rated this menu yet!'
    if rating == 'null':
        return addedText + f"\n\nCurrent rating: No ratings yet!" 
    else:
        return f'<b>{menuItem} Menu Items:</b>\n\n' +  addedText + f"\n\nCurrent rating: ★<b> {rating}</b> ({number_people_rated})"

def cumulativeRating_text():
    return f"Here are the cumulative ratings of the menus this week"

def help_text():
    return f'What can this bot do?\n' + '• Allows you to view breakfast and dinner menu!\n' + '• Do attach a picture of the menu items if no one has done so!\n' + '• Allows you to rate menu items by category!\n' + '• Breakfast winner and dinner winner announced daily and weekly?\n'