""" Terminal view module """

def length(album_list):
    lenght = []
    for i in range(len(album_list[0])):
        size = 0
        for album in album_list:
            if size < len(str(album[i])):
                size = len(album[i])
        lenght.append(size)
    return lenght


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print_list = [title_list] + table
    counter = 0
    add_space = 4
    sum = 0
    pause1 = ""
    pause2 = "/"
    x = length(print_list)
    for item in x:
        sum = sum + int(item)

    sum = sum + add_space + 12

    for item in x:
        pause1 = pause1 + '|' + (item + add_space) * '-'
        pause2 = pause2 + (item + add_space + 1) * '-'

    pause1 = pause1 + '|' + '\n'
    pause2 = pause2[:-1]
    pause2 = pause2 + '\\' + '\n'

    string = pause2

    for items in print_list:
        for item in items:
            string = string + "|{:^{x}}".format(item, x=x[counter] + add_space)
            counter += 1
        string = string + "|" + '\n' + pause1
        counter = 0
    print(string)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(str(label) + ": " + str(result))


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    print(title)
    for i in range(len(list_options)):
        print("{:>5}".format('(') + str(i + 1) + ") " + str(list_options[i]))
    print("{:>5}".format('(') + "0) " + exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    # your code # !!!foolproof to add!!!
    print(title)
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i] + " "))
    return inputs


def get_choice(options):
    print_menu("Main menu", options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    print("<error>" + message + "<error>")
