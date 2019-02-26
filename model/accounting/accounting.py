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
#from model import data_manager
#from model import common



def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    
    >>> add([["c", "d"]], ["a", "b"])
    [['c', 'd'], ['a', 'b']]
    >>> add([], ["a", "b"])
    [['a', 'b']]
    >>> add([], ['a'])
    [['a']]
    >>> add([], [])
    [[]]
    """

    output_table = table.copy()
    output_table.append(record)
    return output_table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    >>> remove([['c', 'd'], ['a', 'b']], 1)
    [['c', 'd']]
    >>> remove([["a", "b"]], 0)
    []
    >>> remove([[]], 0)
    []
    >>> remove([['a']], "a")
    >>> remove([['a']], -3)
    >>> remove([['a']], 1)
    """

    if type(id_) != int: return
    if len(table) <= id_ or id_ < 0: return
    
    output_table = table.copy()
    del output_table[id_]
    return output_table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
