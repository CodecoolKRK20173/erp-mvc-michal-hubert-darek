""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common


# special functions:
# ------------------
def get_data():
    return data_manager.get_table_from_file("model/store/games.csv")


def new_record(inputs, filename):
    new_table_value = []
    new_table_value = common.add(get_data(), make_record(get_data(), inputs))
    data_manager.write_table_to_file(filename, new_table_value)


def delete_record(table, id, filename):
    counter = 0
    remove_id = None
    for item in table:
        if str(item[0]) in str(id):
            remove_id = counter
        counter += 1
    new_list = common.remove(table, remove_id)
    data_manager.write_table_to_file(filename, new_list)


def update_record(table, id, inputs, filename):
    s = "".join(id)
    counter = 0
    update_id = None
    for item in table:
        if str(item[0]) in str(id):
            update_id = counter
        counter += 1
    new_list = common.update(table, update_id, make_record(get_data(), inputs))
    data_manager.write_table_to_file(filename, new_list)


def make_record(table, inputs):
    output_list = [common.generate_random(table)] + inputs
    return output_list


def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    dict_manufactures = {}
    count = 0
    countup = 1
    for items in table:
        if items[2] in dict_manufactures:
            count = countup + dict_manufactures[items[2]]
            dict_manufactures[items[2]] = count
        else:
            dict_manufactures[items[2]] = 1

    return dict_manufactures


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
    stock = 0
    counter = 0
    isManufa = False
    for items in table:
        if items[2] in manufacturer:
            stock = stock + int(items[4])
            counter += 1
            isManufa = True
        if isManufa:
            return stock / counter
        else:
            return "Select manufacturer not exist "
