from datetime import datetime

time = datetime.now().strftime('%H:%M')
print(time)


title = "ATM"
print(title.center(9,'*'))      # making title

user_id = input("Enter your ID: ")
user_pass = input("Enter you password: ")
if int(user_id) == 2222 and int(user_pass) == 3333:     # check if ID and Pass True
    print("GOOD PASS. Welcome!")
else:
    print("Something wrong with your ID or PASS. Try again")
