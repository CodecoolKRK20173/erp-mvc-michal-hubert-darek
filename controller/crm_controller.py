# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    menu_sale = ["Print store list", "Add to store list", "Remove form store list", "Update record in store list",
                 "Show subscribers", "Show longest name ID"]
    title = ["ID", "Name", "E-mail",  "Subscribed"]
    title_del = ["Input ID: "]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)

        if choice == "1":
            terminal_view.print_table(crm.get_data(), title)

        if choice == "2":
            crm.new_record(common.get_user_inp_record(terminal_view.get_inputs(title[1:], "")),
                           "model/crm/customers.csv")
        if choice == "3":
            crm.delete_record(crm.get_data(),
                              common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                              "model/crm/customers.csv")
        if choice == "4":
            crm.update_record(crm.get_data(),
                              common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                              terminal_view.get_inputs(title[1:], ""), "model/crm/customers.csv")
        if choice == "5":
            terminal_view.print_result(crm.get_subscribed_emails(crm.get_data()), "Subscribers")
        if choice == "6":
            terminal_view.print_result(crm.get_longest_name_id(crm.get_data()), "Longest name ID")
