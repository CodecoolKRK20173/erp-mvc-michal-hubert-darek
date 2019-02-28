# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
    menu = ["Show year with highest profit", "Show average profit per item in a given year"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu)
        if choice == "1":
            terminal_view.print_result(accounting.which_year_max(accounting.get_file()), "Year with max profit")
        elif choice == "2":
            year = terminal_view.get_inputs(["Year:"], "")
            terminal_view.print_result(accounting.avg_amount(accounting.get_file(), year[0]), "Averange profit per item")
        else:
            terminal_view.print_error_message("There is no such choice.")
