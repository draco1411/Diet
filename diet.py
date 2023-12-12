import datetime as dt
import json
import os
# import shutil
from FOOD_LIST import FOOD_LIST
from FOOD_LIST import NAME_LIST

# Time retrieval and formatting
date = dt.date.today().strftime("%m-%d-%Y")

weight_path = "/Users/jackbrolin/diet/weight.json"
master_log_path = "/Users/jackbrolin/diet/master_log.json"


def quick_add_list_printer():
    os.system('clear')
    for row in NAME_LIST:
        print("{: <30} {: <30} {: <30}".format(*row))


def log_writer(file_path: str, food: list) -> None:
    with open(file_path, 'r') as file:
        data = json.load(file)
    if data[-1]['date'] == date:
        part = [x + y for x, y in zip(data[-1]['N_vector'], food)]
        data[-1]['N_vector'] = part
        print(f'Total N-Vector for {date}: {part}')
        with open(file_path, 'w') as file:
            json.dump(data, file)
    else:
        row = {'date': f'{date}', 'N_vector': food}
        data.append(row)
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f'Total N-vector for {date}: {food}')
    return None


def quick_add():
    quick_add_list_printer()
    indicator = str(input("Number:  "))
    log_writer(master_log_path, FOOD_LIST[indicator])


def manual_entry():
    cals = int(input("Cal:  "))
    fat = int(input("Fat:  "))
    carbs = int(input("Carbs:  "))
    protein = int(input("Protein:  "))
    log_writer(master_log_path, [cals, fat, carbs, protein])


def weigh_in():
    with open(weight_path, 'r') as file:
        data = json.load(file)
    if data[-1]['date'] == date:
        weight = data[-1]['weight']
        print(f'Already done: on {date} you weigh {weight}')
    else:
        value = float(input('Enter daily weight:  '))
        row = {'date': f'{date}', 'weight': value}
        data.append(row)
        with open(weight_path, 'w') as file:
            json.dump(data, file, indent=2)
    return None


def stats():
    pass


if __name__ == "__main__":
    os.system('clear')
    menu = [
        ['1', 'Quick Add'],
        ['2', 'Manual Entry'],
        ['3', 'Weight-in'],
        ['4', 'Stats']
    ]
    for row in menu:
        print("{: <20} {: <20}".format(*row))

    menu_selection = int(input("Add value:  "))
    menu_selector = [quick_add, manual_entry, weigh_in, stats]
    function = menu_selector[menu_selection - 1]
    function()
