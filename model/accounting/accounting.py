""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common

# special functions:
# ------------------

def get_data():
    return data_manager.get_table_from_file("model/accounting/items.csv")


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
            new_list = common.update(table, update_id, make_record(get_data(), inputs))
        counter += 1
    data_manager.write_table_to_file(filename, new_list)


def make_record(table, inputs):
    output_list = [common.generate_random(table)] + inputs
    return output_list


def calculate_profit(table):
    '''
    Calculate profit in all years

    >>> calculate_profit([["kH14Ju#&", "1", "21", "2137", "out", "100"], ["kH38Jm#&", "10", "23", "1939", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2137", "in", "400"], ["kH38Ju#&", "3", "10", "1939", "in", "100"]])
    {2137: 300.0, 1939: 0.0}
    '''
    __YEAR_INDEX = 3
    __TYPE_INDEX = 4
    __INCOME_INDEX = 5
    years = dict.fromkeys([int(table[index][__YEAR_INDEX]) for index in range(len(table))], 0)
    keys = list(years.keys())
    for record in table:
        if record[__TYPE_INDEX] == "out":
            in_or_out = -1
        else:
            in_or_out = 1
        years[int(record[3])] += float(record[__INCOME_INDEX]) * in_or_out
    return years


def which_year_max(table):
    '''
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number

    >>> which_year_max([["kH14Ju#&", "1", "21", "2137", "out", "100"], ["kH38Jm#&", "10", "23", "1939", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2137", "in", "400"], ["kH38Ju#&", "3", "10", "1939", "in", "100"]])
    2137
    ''' 
    years = calculate_profit(table) 
    highest_profit = next(iter(years.values()))

    for value in years.values():
        if highest_profit < value:
            highest_profit = value

    for key in years.keys():
        if highest_profit == years[key]:
            return key


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    
    >>> avg_amount([["kH14Ju#&", "1", "21", "2137", "out", "100"], ["kH38Jm#&", "10", "23", "1939", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2137", "in", "400"], ["kH38Ju#&", "3", "10", "1939", "in", "100"]], 1939)
    0
    >>> avg_amount([["kH14Ju#&", "1", "21", "2137", "out", "100"], ["kH38Jm#&", "10", "23", "1939", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2137", "in", "400"], ["kH38Ju#&", "3", "10", "1939", "in", "100"]], 2137)
    150
    """
    __YEAR_INDEX = 3
    
    try:
        year = int(year)
    except:
        raise

    profit_in_all_years = calculate_profit(table)
    if not year in profit_in_all_years.keys(): return
    profit_in_chose_year = profit_in_all_years[year]

    amount = 0
    for record in table:
        if int(record[__YEAR_INDEX]) == year:
            amount += 1

    if amount == 0:
        return 0

    average = profit_in_chose_year / amount

    if average == int(average):
        return int(average)
    else:
        return round(average, 3)