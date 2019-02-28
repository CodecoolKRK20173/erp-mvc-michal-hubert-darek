# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    menus = ["Availble items", "Average durability"]
    choice = None
    titles = ["id", "game", "producent", "year", "durability"]
    while choice != "0":
        choice = terminal_view.get_choice(menus)
        if choice == "1":
            terminal_view.print_result(str(inventory.get_available_items(inventory.get_file())), "Availble items: ")
        elif choice == "2":
            terminal_view.print_result(str(inventory.get_average_durability_by_manufacturers(inventory.get_file())), "Oldest persons: ")
        else:
            terminal_view.print_error_message("There is no such choice.")