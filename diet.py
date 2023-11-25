import datetime as dt
import csv
import os
import shutil
from FOOD_LIST import FOOD_LIST

# Time retrieval and formatting
d = dt.date.today()
date = d.strftime("%m-%d-%Y")

current_time = dt.datetime.now().time()
time = current_time.strftime("%I:%M%p")


def quick_add():
    indicator = input("Quick add:  ")
    N_vector = FOOD_LIST[indicator]
    row = (date, time, N_vector)
    with open('food_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    return None


def manual_entry():
    cals = int(input("Cal:  "))
    fat = int(input("Fat:  "))
    carbs = int(input("Carbs:  "))
    protein = int(input("Protein:  "))
    N_vector = [cals, fat, carbs, protein]
    row = (date, time, N_vector)
    with open('food_log.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    return None


def weigh_in():
    daily_weight = int(input("Weight:  "))
    row = (date, daily_weight)
    with open('weight.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    return None


def stats():
    os.system('clear')
    with open('food_log.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    txt = "This is the weather"
    print(txt.center(shutil.get_terminal_size().columns))


menu_selector = [quick_add, manual_entry, weigh_in, stats]


menu_selection = int(input("Select an option: \n"
                           "1: Quick add. \n"
                           "2: Manual Entry \n"
                           "3: Weigh In \n"
                           "4: Stats \n"
                           "Select:  "))


function = menu_selector[menu_selection - 1]
function()
