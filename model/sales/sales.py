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


def new_record(inputs, filename):
    new_table_value = []
    new_table_value = common.add(get_data(), make_record(get_data(), inputs))
    data_manager.write_table_to_file(filename, new_table_value)


def delete_record(table, id, filename):
    s = "".join(id)
    counter = 0
    remove_id = None
    for item in table:
        if str(item[0]) in str(s):
            remove_id = counter
            new_list = common.remove(table, remove_id)
        counter += 1
    data_manager.write_table_to_file(filename, new_list)


def update_record(table, id, inputs, filename):
    counter = 0
    update_id = None
    for item in table:
        if str(item[0]) in str(id):
            update_id = counter
        counter += 1
    new_list = common.update(table, update_id, make_record(get_data(), inputs))
    data_manager.write_table_to_file(filename, new_list)


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


def make_record(table, inputs):
    output_list = [common.generate_random(table)] + inputs
    return output_list


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
    final_filtered_table = []
    for item in table:
        date_inc = (int(item[5]) * 365) + (int(item[3]) * 31) + int(item[4])
        if int(date_inc) > start_date and int(date_inc) < end_date:
            filtered_table.append(item)

    for item in filtered_table:
        item[2] = int(item[2])
        item[3] = int(item[3])
        item[4] = int(item[4])
        item[5] = int(item[5])
        final_filtered_table.append(item)
    return final_filtered_table
