""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
from model import data_manager
from model import common

# special functions:
# ------------------


def get_file():
    imported_file = data_manager.get_table_from_file("model/inventory/inventory.csv")
    return imported_file


def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    durability = table[0][3]
    items_list = []
    final_item_list = []
    for item in table:
        if(durability < item[3]):
            durability = item[3]
    for item in table:
        if(durability == item[3]):
            items_list.append(item)
    for items in items_list:
        items[3] = int(items[3])
        items[4] = int(items[4])
        final_item_list.append(items)
    return final_item_list


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    __MANUFACTURER_INDEX = 2
    tmp_dict = dict.fromkeys([table[index][__MANUFACTURER_INDEX] for index in range(len(table))], 0)
    tmp_dict_count = dict.fromkeys([table[index][__MANUFACTURER_INDEX] for index in range(len(table))], 0)
    result = {}
    durability_sum = 0
    counter = 0
    for item in table:
        name = item[__MANUFACTURER_INDEX]
        tmp_dict[name] += int(item[4])
        tmp_dict_count[name] += 1
    for k, v in tmp_dict.items():
        result[k] = v/tmp_dict_count[k]
    return result