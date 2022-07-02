import database


MENU_PROMPT = """
PLEASE CHOSE ONE OF THESE OPTIONS:
1) ADD A NEW BEAN.
2) SEE ALL BEANS
3) FIND A BEAN BY NAME
4) SEE WHICH PREPARATION METHOD IS BEST FOR A BEAN
5) EXIT

YOUR SELECTION:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean(connection)
        elif user_input == "4":
            prompt_find_best_method(connection)
        else:
            print("invalid input, please try again")


def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you should prepare it: ")
    rating = int(input("Enter your rating score (0-100)"))

    database.add_bean(connection, name, method, rating)


def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = database.get_beans_by_name(connection, name)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_best_method(connection):
    name = input("Enter name to find: ")
    best_method = database.get_best_preparation_for_bean(connection, name)

    print(f"The best preparation method for {name} is: {best_method[2]}")

menu()