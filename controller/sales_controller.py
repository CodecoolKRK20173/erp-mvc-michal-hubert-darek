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


    # your code
    menu_sale = ["Print sale list", "Add to sale list", "Remove form sale list", "Update record in sale list",
                 "Get ID lowest price item", "Get Item/s between date"]
    title = ["ID", "Title", "Price", "Month", "Day", "Year"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)

        if choice == "1":
            terminal_view.print_table(sales.get_data(),title)

        if choice == "2":
            pass

        if choice == "3":
            pass

        if choice == "4":
            pass

        if choice == "5":
            terminal_view.print_result(sales.get_lowest_price_item_id(sales.get_data()),
                                       'Id of the item sold the cheapest')
        if choice == "6":
            user_input_list = get_user_inp()
            print("DUPA")
            print(user_input_list)
            print("DUPA")
            print(user_input_list[0])
            terminal_view.print_table(
                sales.get_items_sold_between(sales.get_data(), user_input_list[0], user_input_list[1],
                                             user_input_list[2], user_input_list[3], user_input_list[4],
                                             user_input_list[5]), title)
