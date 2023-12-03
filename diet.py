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
    with open('daily_log.json', 'a') as file:
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
    with open('daily_log.json', 'a') as file:
        json.dump(row, file)
        file.write('\n')
    return None


def aux_file_writer():
    with open('/Users/jackbrolin/diet/master_log.json', 'a') as file:
        for i in range(1,  31):
            current_date = dt.date(2024, 4, i)
            row = {"date": str(current_date.strftime("%m-%d-%Y")), "N-vector":
                   [0, 0, 0, 0]}
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


def get_weight():
    with open('/Users/jackbrolin/diet/weight.json', 'r') as file:
        data = [json.loads(line) for line in file]
        daily_weight = [data[i]['weight'] for i in range(len(data))]
        print(daily_weight)
    return None


def get_daily_food():
    with open('/Users/jackbrolin/diet/daily_log.json', 'r') as file:
        data = [json.loads(line) for line in file]
        partial = [data[i]['N_vector'] for i in range(len(data))]
        total_cals = [partial[i][0] for i in range(len(partial))]
        print(sum(total_cals))
    return None


def stats():
    os.system('clear')
    get_weight()
    get_daily_food()
    return None


# menu_selector = [quick_add, manual_entry, weigh_in, stats]

os.system('clear')
# menu_selection = int(input("Select an option: \n"
#                            "1: Quick add. \n"
#                            "2: Manual Entry \n"
#                            "3: Weigh In \n"
#                            "4: Stats \n"
#                            "Select:  "))

aux_file_writer()

# function = menu_selector[menu_selection - 1]
# function()
