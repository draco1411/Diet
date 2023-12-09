import datetime as dt
import json
import os
# import shutil
from FOOD_LIST import FOOD_LIST

# Time retrieval and formatting
date = dt.date.today().strftime("%m-%d-%Y")


def log_writer(food):
    row = {f"{date}": food}
    with open("/Users/jackbrolin/diet/master_log.json", "r") as file:
        data = json.load(file)
    if any(date in entry for entry in data):  # instantiated
        for entry in data:
            if date in entry:
                part = [el1 + el2 for el1, el2 in zip(entry[f"{date}"], food)]
                entry[f"{date}"] = part
            break
        with open("/Users/jackbrolin/diet/master_log.json", "w") as file:
            json.dump(data, file)
    else:  # Not instantiated
        with open("/Users/jackbrolin/diet/master_log.json", "r") as file:
            data = json.load(file)
        data.append(row)
        with open("/Users/jackbrolin/diet/master_log.json", "r") as file:
            json.dump(data, file)


def quick_add():
    indicator = str(input("Number:  "))
    log_writer(FOOD_LIST[indicator])


def manual_entry():
    cals = int(input("Cal:  "))
    fat = int(input("Fat:  "))
    carbs = int(input("Carbs:  "))
    protein = int(input("Protein:  "))
    N_vector = [cals, fat, carbs, protein]
    log_writer(N_vector)


def weigh_in():
    weight = int(input("Weight:  "))
    row = {f"{date}": weight}
    with open("/Users/jackbrolin/diet/weight.json", "r") as file:
        data = json.load(file)
    if any(date in entry for entry in data):
        print("already done today")
    else:
        with open("/Users/jackbrolin/diet/weight.json", "r") as file:
            data = json.load(file)
        data.append(row)
        with open("/Users/jackbrolin/diet/weight.json", "w") as file:
            json.dump(data, file, indent=2)


menu_selector = [quick_add, manual_entry, weigh_in]

os.system('clear')
menu_selection = int(input("Select an option: \n"
                           "1: Quick add. \n"
                           "2: Manual Entry \n"
                           "3: Weigh In \n"
                           "4: Stats \n"
                           "Select:  "))


function = menu_selector[menu_selection - 1]
function()
