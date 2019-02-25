""" Common functions for models
implement commonly used functions here
"""
import random


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

print(generate_random(["kH94Ju#&"]))