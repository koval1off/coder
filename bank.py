from datetime import datetime

time = datetime.now().strftime('%H:%M')
print(time)

title = "ATM"
print(title.center(9, '*'))      # making title

user_balance = 5000


def check_id_and_pin(user_id, user_pin):
    if user_id == 2222 and user_pin == 3333:
        return True

    return False


def change_balance(new_balance):
    if new_balance < 0:
        print('Cannot update balance. Reason: New balance is negative')
        return

    global user_balance
    user_balance = new_balance


def upload_money(amount):
    if amount <= 0:
        print('You must upload more than 0')
        return

    new_balance = user_balance + amount
    change_balance(new_balance)


def withdrawal_money(amount):
    if amount <= 0:
        print('You must withdrawal more than 0')
        return

    if user_balance < amount:
        print('You want to withdrawal more than you have')
        return

    new_balance = user_balance - amount
    change_balance(new_balance)


def show_balance():
    print(f"You choosed the Show balance operation!\n"
          f"Your current balance is {user_balance}")


def get_number_from_input(text):
    num = input(text)

    return int(num)


def menu():
    while True:
        print("Menu:\n\t"
              "1) Upload money\n\t"
              "2) Withdrawal money\n\t"
              "3) Show balance\n\t"
              "4) Exit\n\t")   # show the menu operations

        menu_choise = input("Enter the number of operation: ")
        if int(menu_choise) == 1:
            amount = get_number_from_input("Enter amount you wanna upload: ")
            upload_money(amount)
            show_balance()
        elif int(menu_choise) == 2:
            amount = get_number_from_input("Enter amount you wanna withdrawal: ")
            withdrawal_money(amount)
            show_balance()
        elif int(menu_choise) == 3:
            show_balance()
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
