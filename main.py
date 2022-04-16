from bank import ATM
from datetime import datetime


def check_id_and_pin(user_id, user_pin):
    if user_id == 2222 and user_pin == 3333:
        return True

    return False


def get_number_from_input(text):
    num = input(text)

    return int(num)


def menu():
    privat_bank_atm = ATM()

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
            privat_bank_atm.upload_money(amount)
            privat_bank_atm.show_balance()
        elif int(menu_choise) == 2:
            amount = get_number_from_input("Enter amount you wanna withdrawal: ")
            privat_bank_atm.withdrawal_money(amount)
            privat_bank_atm.show_balance()
        elif int(menu_choise) == 3:
            privat_bank_atm.show_balance()
        elif int(menu_choise) == 4:
            return
        else:
            print('Wrong command, try again')


def main():
    user_id = get_number_from_input("Enter your ID: ")
    user_pass = get_number_from_input("Enter you password: ")

    if not check_id_and_pin(user_id, user_pass):
        print("Something wrong with your ID or PASS. Try again")
        return

    print('Welcome to our Bank!')
    menu()


main()