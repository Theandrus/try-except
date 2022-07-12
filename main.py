from user_functions import *

while True:
    print("1. Add New User\n"
           + "2. Get All Users\n"
           + "3. Search\n"
           + "4. Update User By Id"
          )
    try:
        menu_flag = int(input("Type your choose: "))

        if menu_flag == 1:
            user_add()
        elif menu_flag == 2:
            get_all()
        elif menu_flag == 3:
            what_to_search = input('By Which Parametr you want to search(first_name, last_name, Email, id): ')
            search_str = input('Search: ')
            search_by(search_str, what_to_search)
        elif menu_flag == 4:
            update_user()
    except ValueError:
        print("Sorry. Enter a number(1-4), not anything else")