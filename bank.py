from datetime import datetime

time = datetime.now().strftime('%H:%M')
print(time)

title = "ATM"
print(title.center(9,'*'))      # making title

user_balance = 5000
user_id = input("Enter your ID: ")
user_pass = input("Enter you password: ")

def change_balance():
    print("You choosed change balance operation!")
    global user_balance
    balance_changes = input("Enter changes you wanna make: ")
    user_balance += int(balance_changes)   # upgrade balance
    if user_balance < 0:
        print("Too much to withdraw!")
    # else:
    #     print(f"The new balance is {user_balance}")
    menu()

def show_balance():
    print(f"You choosed the Show balance operation!\nYour current balance is {user_balance}")
    menu()

def menu():
    print("Menu:\n\t1) Change the balance\n\t2) Show new balance")   # show the menu operations
    menu_choise = input("Enter the number of operation: ")
    if int(menu_choise) == 1:
        change_balance()
    elif int(menu_choise) == 2:
        show_balance()

if int(user_id) == 2222 and int(user_pass) == 3333:     # check if ID and Pass True
    print("GOOD PASS. Welcome!")
else:
    print("Something wrong with your ID or PASS. Try again")

menu()