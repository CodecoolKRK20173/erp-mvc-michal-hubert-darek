# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
    menus = ["Option 1 hr", "Option 2 hr"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menus)
        if choice == "1":
            inventory.get_available_items()
        elif choice == "2":
            inventory.get_average_durability_by_manufacturers()
        else:
            terminal_view.print_error_message("There is no such choice.")