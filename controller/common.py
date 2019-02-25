""" Common functions for controllers
implement commonly used functions here
"""

def quicksort(table_to_sort, ascending_order = True):
    if not table_to_sort: return []
    if len(table_to_sort) == 1: return table_to_sort

    pivot_element = table_to_sort.pop(0)
    lower_elements = [element for element in table_to_sort if element <= pivot_element]
    higher_elements = [element for element in table_to_sort if element > pivot_element]

    if not ascending_order: 
        lower_elements, higher_elements = higher_elements, lower_elements

    return quicksort(lower_elements, ascending_order) + [pivot_element] + quicksort(higher_elements, ascending_order)
