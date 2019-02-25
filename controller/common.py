""" Common functions for controllers
implement commonly used functions here
"""

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
    '''
    index = 0
    if name_of_element in list_of_elements:
        for element in list_of_elements:
            if name_of_element == element:
                return index
            index += 1
    else:
        return None
