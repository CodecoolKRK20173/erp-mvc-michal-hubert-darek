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
    menus = ["Oldest employe", "Average age"]
    choice = None
    titles = ["id", "name", "year"]
    while choice != "0":
        choice = terminal_view.get_choice(menus)
        if choice == "1":
            terminal_view.print_table(hr.get_oldest_person(hr.get_file()), titles)
        elif choice == "2":
            terminal_view.print_table(hr.get_persons_closest_to_average(hr.get_file()), titles)
        else:
            terminal_view.print_error_message("There is no such choice.")
