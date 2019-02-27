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

    # your code
    menu_sale = ["Get ID lowest price item", "Get Item/s between date"]
    title = ["ID", "Title", "Price", "Month", "Day", "Year"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(menu_sale)
        if choice == "1":
            terminal_view.print_result(sales.get_lowest_price_item_id(sales.get_data()),
                                       'Id of the item sold the cheapest')
        if choice == "2":
            user_input_list = sales.get_user_input()
            print(user_input_list[0])
            terminal_view.print_table(
                sales.get_items_sold_between(sales.get_data(), user_input_list[0], user_input_list[1],
                                             user_input_list[2], user_input_list[3], user_input_list[4],
                                             user_input_list[5]), title)
