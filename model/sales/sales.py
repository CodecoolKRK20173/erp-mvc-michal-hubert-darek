""" Sales module

Data table structure:
  0  * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
  1  * title (string): Title of the game sold
  2  * price (number): The actual sale price in USD
  3  * month (number): Month of the sale
  4  * day (number): Day of the sale
  5  * year (number): Year of the sale
"""

# everything you'll need is imported:
from model import data_manager
from model import common

import os


# ------------------

def get_data():
    return data_manager.get_table_from_file("model/sales/sales.csv")


def get_user_input():
    input_list = []
    title_list = ["month_from: ", "day_from: ", "year_from: ", "month_to: ", "day_to: ", "year_to: "]
    try:
        for i in range(0, 6):
            user_input = input(title_list[i])
            val = int(user_input)
            input_list.append(int(val))
    except ValueError:
        input_list.clear()
        return get_user_input()
    return input_list


def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code

    minimal_price = table[0][2]
    item_id = table[0][0]

    for item in table:
        if minimal_price > item[2]:
            minimal_price = item[2]
            item_id = item[0]
    return item_id


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
    start_date = (year_from * 365) + (month_from * 31) + day_from
    end_date = (year_to * 365) + (month_to * 31) + day_to
    filtered_table = []
    for item in table:
        date_inc = (int(item[5]) * 365) + (int(item[3]) * 31) + int(item[4])
        if int(date_inc) >= start_date and int(date_inc) <= end_date:
            filtered_table.append(item)
    return filtered_table
