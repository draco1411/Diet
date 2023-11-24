# import json as js
import datetime as dt


def quick_add():
    print("This returns for quick add")
    return None


def manual_entry():
    print("This returns for manual_entry")
    return None


def weigh_in():
    daily_weight = int(input("Weight:  "))
    date = dt.date.today()
    with open('diet.csv', 'a') as file:
        file.write(f"{date},{daily_weight}")
    print(daily_weight)
    print(date)
    return None


menu = {
    "1": "Quick add",
    "2": "Manual",
    "3": "Weigh In"
}

menu_selector = [quick_add, manual_entry, weigh_in]

QUICK_FOOD_LIST = {
    "1": [],  # Greek Yogurt w/ Honey
    "2": [],  # P-Shake
    "3": [],  # Two Burger Dinner
    "4": [],  # 170g Cottage Cheese
    "5": [],  # Standard Cereal
    "6": [],  # 4 Egg w/ Cheese Lunch

}


menu_selection = int(input("Select an option: \n"
                           "1: Quick add. \n"
                           "2: Manual Entry \n"
                           "3: Weigh In \n"
                           "Select:  "))


function = menu_selector[menu_selection - 1]
function()
