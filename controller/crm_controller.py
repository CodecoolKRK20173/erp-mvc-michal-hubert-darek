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

    menu = ["Show subscribers", "Show id of person with the longest surname"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu)
        if choice == "1":
            terminal_view.print_result(crm.get_subscribed_emails(crm.get_file()), "Subscribers")
        elif choice == "2":
            terminal_view.print_result(crm.get_longest_name_id(crm.get_file()), "Id of person with the longest surname")
        else:
            terminal_view.print_error_message("There is no such choice.")
