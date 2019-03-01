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

    menu_store = ["Print store list", "Add to store list", "Remove form store list", "Update record in store list",
                  "Number of games in the manufacture", "Average amount of games in stock of a given manufacturer "]
    title = ["ID", "Title", "Manufacturer", "Price", "In_stock"]
    title_del = ["Input ID: "]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_store)

        if choice == "1":
            terminal_view.print_table(store.get_data(), title)

        if choice == "2":
            store.new_record(common.get_user_inp_record(terminal_view.get_inputs(title[1:], "")),
                             "model/store/games.csv")
        if choice == "3":
            store.delete_record(store.get_data(), common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                "model/store/games.csv")
        if choice == "4":
            store.update_record(store.get_data(), common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                terminal_view.get_inputs(title[1:], ""), "model/store/games.csv")
        if choice == "5":
            terminal_view.print_result(store.get_counts_by_manufacturers(store.get_data()),
                                       "Different kinds of game are available of each manufacturer: ")
        if choice == "6":
            terminal_view.print_result(store.get_average_by_manufacturer(store.get_data(), common.get_user_inp_record(
                terminal_view.get_inputs(["Input manufactures: "], ""))), "Average games in manufacturer: ")
