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

def calculate_profit(table):
    '''
    Calculate profit in all years

    >>> calculate_profit([["kH14Ju#&", "1", "21", "2015", "out", "100"], ["kH38Jm#&", "10", "23", "2016", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2015", "in", "400"], ["kH38Ju#&", "3", "10", "2016", "in", "100"]])
    {2015: 300.0, 2016: 0.0}
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

    >>> which_year_max([["kH14Ju#&", "1", "21", "2015", "out", "100"], ["kH38Jm#&", "10", "23", "2016", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2015", "in", "400"], ["kH38Ju#&", "3", "10", "2016", "in", "100"]])
    2015
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
    
    >>> avg_amount([["kH14Ju#&", "1", "21", "2015", "out", "100"], ["kH38Jm#&", "10", "23", "2016", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2015", "in", "400"], ["kH38Ju#&", "3", "10", "2016", "in", "100"]], 2016)
    0
    >>> avg_amount([["kH14Ju#&", "1", "21", "2015", "out", "100"], ["kH38Jm#&", "10", "23", "2016", "out", "100"],\
    ["eH34Jd#&", "2", "12", "2015", "in", "400"], ["kH38Ju#&", "3", "10", "2016", "in", "100"]], 2015)
    150
    """
    __YEAR_INDEX = 3
    profit_in_all_years = calculate_profit(table)
    
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
        return average