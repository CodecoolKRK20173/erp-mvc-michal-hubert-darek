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
    menu_sale = ["Print sale list", "Add to sale list", "Remove form sale list", "Update record in sale list",
                 "Oldest employe", "Average age"]
    title = ["Id", "Name", "Year"]
    title_del = ["Input ID: "]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)

        if choice == "1":
            terminal_view.print_table(hr.get_data(), title)

        if choice == "2":
            hr.new_record(common.get_user_inp_record(terminal_view.get_inputs(title[1:], "")),
                          "model/hr/persons.csv")

        if choice == "3":
            hr.delete_record(hr.get_data(), common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                             "model/hr/persons.csv")

        if choice == "4":
            hr.update_record(hr.get_data(), common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                             terminal_view.get_inputs(title[1:], ""), "model/hr/persons.csv")

        if choice == "5":
            terminal_view.print_result(str(hr.get_oldest_person(hr.get_data())), "Oldest persons: ")
        if choice == "6":
            terminal_view.print_result(str(hr.get_persons_closest_to_average(hr.get_data())),
                                       "Closest to average age: ")
