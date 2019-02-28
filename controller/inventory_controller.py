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

    menu_sale = ["Print store list", "Add to store list", "Remove form store list", "Update record in store list",
                 "Availble items", "Average durability"]
    title = ["ID", "Title", "Producer", "Year", "Durability"]
    title_del = ["Input ID: "]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)

        if choice == "1":
            terminal_view.print_table(inventory.get_data(), title)

        if choice == "2":
            inventory.new_record(common.get_user_inp_record(terminal_view.get_inputs(title[1:], "")),
                                 "model/inventory/inventory.csv")
        if choice == "3":
            inventory.delete_record(inventory.get_data(),
                                    common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                    "model/inventory/inventory.csv")
        if choice == "4":
            inventory.update_record(inventory.get_data(),
                                    common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                    terminal_view.get_inputs(title[1:], ""), "model/inventory/inventory.csv")
        if choice == "5":
            terminal_view.print_result(str(inventory.get_available_items(inventory.get_data())), "Availble items: ")
        if choice == "6":
            terminal_view.print_result(str(inventory.get_average_durability_by_manufacturers(inventory.get_data())),
                                       "Oldest persons: ")
