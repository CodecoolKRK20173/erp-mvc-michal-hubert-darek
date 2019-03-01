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
    menu_accounting = ["Print accounting list", "Add to accounting list", "Remove form accounting list",
                       "Update record in accounting list",
                       "Show year with highest profit", "Show average profit per item in a given year"]
    title = ["Id", "Month", "Day", "Year", "Type", "Amount"]
    title_del = ["Input ID: "]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_accounting)

        if choice == "1":
            terminal_view.print_table(accounting.get_data(), title)

        if choice == "2":
            accounting.new_record(common.get_user_inp_record(terminal_view.get_inputs(title[1:], "")),
                                  "model/accounting/items.csv")

        if choice == "3":
            accounting.delete_record(accounting.get_data(),
                                     common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                     "model/accounting/items.csv")

        if choice == "4":
            accounting.update_record(accounting.get_data(),
                                     common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                     terminal_view.get_inputs(title[1:], ""), "model/accounting/items.csv")

        if choice == "5":
            terminal_view.print_result(accounting.which_year_max(accounting.get_data()), "Year with max profit")
        if choice == "6":
            year = terminal_view.get_inputs(["Year:"], "")
            terminal_view.print_result(accounting.avg_amount(accounting.get_data(), year[0]),
                                       "Averange profit per item")
