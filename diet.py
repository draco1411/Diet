import datetime as dt
import json
import os
# import shutil
from FOOD_LIST import FOOD_LIST

# Time retrieval and formatting
d = dt.date.today()
date = d.strftime("%m-%d-%Y")


def quick_add():
    indicator = input("Quick add:  ")
    N_vector = FOOD_LIST[indicator]
    row = {"date": date, "N_vector": N_vector}
    with open('log.json', 'a') as file:
        json.dump(row, file)
        file.write('\n')
    return None


def manual_entry():
    cals = int(input("Cal:  "))
    fat = int(input("Fat:  "))
    carbs = int(input("Carbs:  "))
    protein = int(input("Protein:  "))
    N_vector = [cals, fat, carbs, protein]
    row = {"date": date, "N_vector": N_vector}
    with open('log.json', 'a') as file:
        json.dump(row, file)
        file.write('\n')
    return None


def weigh_in():
    daily_weight = int(input("Weight:  "))
    row = {"date": date, "weight": daily_weight}
    with open('weight.json', 'a') as file:
        json.dump(row, file)
        file.write('\n')
    return None


def stats():
    os.system('clear')
    with open('weight.json', 'r') as file:
        data = [json.loads(line) for line in file]
        daily_weight = [data[i]['weight'] for i in range(len(data))]
        print(daily_weight)
    with open('log.json', 'r') as file:
        data = [json.loads(line) for line in file]
        partial = [data[i]['N_vector'] for i in range(len(data))]
        total_weight = [partial[i][0] for i in range(len(partial))]
        print(sum(total_weight))


menu_selector = [quick_add, manual_entry, weigh_in, stats]

os.system('clear')
menu_selection = int(input("Select an option: \n"
                           "1: Quick add. \n"
                           "2: Manual Entry \n"
                           "3: Weigh In \n"
                           "4: Stats \n"
                           "Select:  "))

function = menu_selector[menu_selection - 1]
function()
