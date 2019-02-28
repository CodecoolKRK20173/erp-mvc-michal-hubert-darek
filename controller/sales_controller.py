# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    def get_user_inp():
        inp_list = []
        title_list = ["month_from: ", "day_from: ", "year_from: ", "month_to: ", "day_to: ", "year_to: "]
        try:
            user_inp = terminal_view.get_inputs(title_list, "")
            val = user_inp
            inp_list = list(map(int, val))
        except ValueError:
            inp_list.clear()
            return get_user_inp()
        return inp_list

    #  def get_user_inp_record(title_list):
    #     inp_list = []
    #     user_inp = terminal_view.get_inputs(title_list, "")
    #     val = user_inp
    #    print(val)
    #    return val

    # your code
    menu_sale = ["Print sale list", "Add to sale list", "Remove form sale list", "Update record in sale list",
                 "Get ID lowest price item", "Get Item/s between date"]
    title = ["ID", "Title", "Price", "Month", "Day", "Year"]
    title_del = ["Input ID: "]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)

        if choice == "1":
            terminal_view.print_table(sales.get_data(), title)

        if choice == "2":
            sales.new_record(common.get_user_inp_record(terminal_view.get_inputs(title[1:], "")),
                             "model/sales/sales.csv")

        if choice == "3":
            sales.delete_record(sales.get_data(), common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                "model/sales/sales.csv")

        if choice == "4":
            sales.update_record(sales.get_data(), common.get_user_inp_record(terminal_view.get_inputs(title_del, "")),
                                terminal_view.get_inputs(title[1:], ""), "model/sales/sales.csv")

        if choice == "5":
            terminal_view.print_result(sales.get_lowest_price_item_id(sales.get_data()),
                                       'Id of the item sold the cheapest')
        if choice == "6":
            user_input_list = get_user_inp()
            terminal_view.print_table(
                sales.get_items_sold_between(sales.get_data(), user_input_list[0], user_input_list[1],
                                             user_input_list[2], user_input_list[3], user_input_list[4],
                                             user_input_list[5]), title)
