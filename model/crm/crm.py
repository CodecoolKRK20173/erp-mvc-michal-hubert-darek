""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common


def get_data():
    return data_manager.get_table_from_file("model/crm/customers.csv")


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


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
    """
    __NAME_INDEX = 1
    max_len = 0
    name_len_dict = {}
    
    for record in table:
        len_of_name = len(record[__NAME_INDEX].split()[1])
        if len_of_name > max_len:
            max_len = len_of_name
            name_len_dict[max_len] = record[0]

    return name_len_dict[max_len]

    


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
    """
    __NAME_INDEX = 1
    __EMAIL_INDEX = 2
    __SUB_FLAG_INDEX = 3
    return([f"{record[__EMAIL_INDEX]};{record[__NAME_INDEX]}" for record in table if int(record[__SUB_FLAG_INDEX])])
