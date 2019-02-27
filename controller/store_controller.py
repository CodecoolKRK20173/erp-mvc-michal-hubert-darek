# everything you'll need is imported:
from model.store import store
from view import terminal_view
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

    menu_sale = ["Print store list", "Add to store list", "Remove form store list", "Update record in store list",
                 "number of games in the manufacture", "Average amount of games in stock of a given manufacturer "]
    title = ["ID", "Title", "Price", "Month", "Day", "Year"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)

        if choice == "1":
            terminal_view.print_table(store.get_data(),title)

        if choice == "2":
            pass

        if choice == "3":
            pass

        if choice == "4":
            pass
        if choice == "5":
            store.get_counts_by_manufacturers(store.get_data())
        if choice == "6":
            pass
