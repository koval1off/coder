from bank import ATM
from datetime import datetime
from user import User


def get_number_from_input(text: str) -> int:
    try:
        num = input(text)
        return int(num)
    except ValueError:
        print("Use 4 digits!")


def validation_credential(user_id: str, user_pin: str) -> bool:
    if len(str(user_id)) == 4 and len(str(user_pin)) == 4:
        return True
    else:
        print("Too long or too short!")
        return False


def menu(user: User, atm: ATM):
    if user is None:
        return

    if atm is None:
        return

    while True:
        time = datetime.now().strftime('%H:%M')
        print(time)

        title = "ATM"
        print(title.center(9, '*'))  # making title
        print("Menu:\n\t"
              "1) Upload money\n\t"
              "2) Withdrawal money\n\t"
              "3) Show balance\n\t"
              "4) Exit\n\t")   # show the menu operations

        menu_choise = input("Enter the number of operation: ")
        if int(menu_choise) == 1:
            amount = get_number_from_input("Enter amount you wanna upload: ")
            atm.upload_money(user, amount)
            atm.show_balance(user)
        elif int(menu_choise) == 2:
            amount = get_number_from_input("Enter amount you wanna withdrawal: ")
            atm.withdrawal_money(user, amount)
            atm.show_balance(user)
        elif int(menu_choise) == 3:
            atm.show_balance(user)
        elif int(menu_choise) == 4:
            return
        else:
            print('Wrong command, try again')


def main():
    atm = ATM()
    user = None
    count_attemps = 1
    login_success = False

    while count_attemps <= 3:
        user_id = input("Enter your ID: ")
        user_pass = input("Enter your PASS: ")

        if validation_credential(user_id, user_pass):
            user = atm.get_user(user_id)
            if user:
                login_success = atm.check_pin(user, user_pass)
            if not login_success:
                error_text = f"Wrong ID or PASS. {count_attemps}/3."
                print(error_text + ' Try again') if count_attemps < 3 else print(error_text)
                count_attemps += 1
            else:
                break
        else:
            continue
    
    if login_success and user:
        menu(user, atm)
    else:
        print("Try next time. Too much fails")


main()