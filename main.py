from bank import ATM
from datetime import datetime


with open("database.txt", "w") as f:    # just to create the file automatically 
    f.write("2222:3333\n")
    f.write("5555:6666\n")


def check_id_and_pin(user_id, user_pin):
    with open("database.txt", "r") as base:
        for line in base.readlines():
            line = line.split(":")
            if str(user_id) in line[0]:
                if str(user_pin) in line[1]:
                    return True


def get_number_from_input(text):
    try:
        num = input(text)
        return int(num)
    except ValueError:
        print("Use 4 digits!")


def validation_credential(user_id, user_pin):
    if len(str(user_id)) == 4 and len(str(user_pin)) == 4:
        return True
    else:
        print("Too long or too short!")
        return False


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
    count_attemps = 1
    login_success = False

    while count_attemps <= 3:
        user_id = get_number_from_input("Enter your ID: ")
        user_pass = get_number_from_input("Enter your PASS: ")

        if validation_credential(user_id, user_pass):
            login_success = check_id_and_pin(user_id, user_pass)
            if not login_success:
                error_text = f"Wrong ID or PASS. {count_attemps}/3."
                print(error_text + ' Try again') if count_attemps < 3 else print(error_text)
                count_attemps += 1
            else:
                break
        else:
            continue
    
    if login_success:
        menu()
    else:
        print("Try next time. Too much fails")


main()