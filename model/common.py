""" Common functions for models
implement commonly used functions here
"""
import random


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    
    >>> add([["record", "one"]], ["new", "record"])
    [['record', 'one'], ['new', 'record']]

    >>> add([], ["new", "record"])
    [['new', 'record']]
    
    >>> add([], ["new", "record"])
    [['new', 'record']]
    
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
        
    >>> remove([["record", "one"], ["record", "two"]], 1)
    [['record', 'one']]
    >>> remove([["record", "one"]], 0)
    []
    >>> remove([[]], 0)
    []
    >>> remove([["record", "one"]], "a")
    >>> remove([["record", "one"]], -3)
    >>> remove([["record", "one"]], 1)
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
    
    >>> update([['record', 'one'], ['record', 'two']], 1, ['new', 'record'])
    [['record', 'one'], ['new', 'record']]

    >>> update([["a", "b"]], 0, [])
    [[]]

    >>> update([[]], 0, ['new', 'record'])
    [['new', 'record']]

    >>> update([['old_record']], "a", ['new_record'])
    [['old_record']]

    >>> update([['old_record']], -3, ['new_record'])
    [['old_record']]
    
    >>> update([['old_record']], 1, ['new_record'])
    [['old_record']]
    """

    if type(id_) != int: return table.copy()
    if len(table) <= id_ or id_ < 0: return table.copy()
    
    output_table = table.copy()
    output_table[id_] = record

    return output_table


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    lower_letter = lambda: chr(random.randint(ord('a'), ord('z')))
    upper_letter = lambda: chr(random.randint(ord('A'), ord('Z')))
    number = lambda: random.randint(0,9)
    
    def special():
        exception = ("+", "-", "=", ";", ":", "'", '"', ",", ".") + tuple(map(str, range(0, 10)))
        generated_special_chr = chr(random.randint(ord('!'), ord('@')))
        while(generated_special_chr in exception):
            generated_special_chr = chr(random.randint(ord('!'), ord('@')))# witouth exception tuple characters
        return generated_special_chr

    generated = f"{lower_letter()}{upper_letter()}{number()}{number()}{upper_letter()}{lower_letter()}{special()}{special()}"

    if generated not in table: 
        return generated# Example kH94Ju#&
    else: 
        try:
            generate_random(table)
        except RecursionError:
            print("Stack overflow error!")