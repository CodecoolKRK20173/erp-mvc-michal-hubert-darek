""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common

# special functions:
# ------------------


def get_data():
    return data_manager.get_table_from_file("model/hr/persons.csv")


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

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    oldest = table[0][2]
    name = table[0][1]
    persons = []
    for item in table:
        if(oldest > item[2]):
            oldest = item[2]
    for item in table:
        if(oldest == item[2]):
            persons.append(item[1])
    return persons


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    tmp_persons = []
    age_of_employee = {}
    age = table[0][2]
    current_year = 2019
    close_enough = 5
    avg_age = 0
    result_age = 0
    counter = 0
    tmp_result = 0
    for item in table:
        result_age = current_year - int(item[2])
        tmp_result = tmp_result + result_age
        counter += 1
    avg_age = tmp_result / counter

    for item in table:
        result_age = current_year - int(item[2])
        age_of_employee[int(abs(result_age - avg_age))] = item[1]
    key = int(min(age_of_employee.keys()))
    output = []
    output.append(age_of_employee[key])
    return output
