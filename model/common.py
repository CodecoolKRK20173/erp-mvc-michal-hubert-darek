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


def quicksort(table_to_sort, ascending_order = True):
    '''
    Sort items with O(n*log(n)) computational complexity

    >>> quicksort([1, 3, 5, 2, 8, 10], ascending_order = True)
    [1, 2, 3, 5, 8, 10]
    >>> quicksort([1, 3, 5, 2, 8, 10], ascending_order = False)
    [10, 8, 5, 3, 2, 1]
    >>> quicksort(['c', 'd' , 'a', 'b'], ascending_order = True)
    ['a', 'b', 'c', 'd']
    >>> quicksort(['c', 'd' , 'a', 'b'], ascending_order = False)
    ['d', 'c', 'b', 'a']
    '''
    if not table_to_sort: return []
    if len(table_to_sort) == 1: return table_to_sort

    pivot_element = table_to_sort.pop(0)
    lower_elements = [element for element in table_to_sort if element <= pivot_element]
    higher_elements = [element for element in table_to_sort if element > pivot_element]

    if not ascending_order: 
        lower_elements, higher_elements = higher_elements, lower_elements

    return quicksort(lower_elements, ascending_order) + [pivot_element] + quicksort(higher_elements, ascending_order)


def find_index(list_of_elements, name_of_element):
    '''
    Try to find first element equal name_of_element in list_of_elements

    >>> find_index([1,2,3,5,7], 3)
    2
    >>> find_index(["g","j","b","c","a"], "c")
    3
    >>> find_index([1,"2","b",5,"b"], "b")
    2
    >>> find_index([1,2,3,5,7], 10)
    >>> find_index([], 10)
    '''
    index = 0
    if name_of_element in list_of_elements:
        for element in list_of_elements:
            if name_of_element == element:
                return index
            index += 1
    else:
        return None

def count_elements(list_of_elements, name_of_element):
    '''
    Count elements equal name_of_element in list_of_elements

    >>> count_elements([1,2,2,2,7], 2)
    3
    >>> count_elements(["g","c","b","c","a"], "c")
    2
    >>> count_elements([1,"2","b",5,"b"], "b")
    2
    >>> count_elements([1,2,3,5,7], 10)
    0
    >>> count_elements([], 10)
    0
    '''
    counter = 0
    for element in list_of_elements:
        if name_of_element == element:
            counter += 1
    return counter

def find_max(list_of_elements):
    '''
    Find max element in list_of_elements

    >>> max([1,2,2,2,7])
    7
    >>> max(["g","c","b","c","a"])
    'g'
    '''
    max = list_of_elements[0]
    for element in elements:
        if not max > element:
            max = element
    return max