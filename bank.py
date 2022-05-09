from user import User


class ATM:
    def __init__(self):
        self.users = []
        self._read_users()

    def _read_users(self):
        """reads file and writes users"""
        with open("database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                info = line.split(":")
                user = User(info[0], info[1], int(info[2]))
                self.users.append(user)

    def print_users(self):
        """prints users' info"""
        for user in self.users:
            print(f"User_ID: {user.user_id}; User_PIN: {user.pin}; User_BALANCE: {user.balance}")

    def get_user(self, user_id: str):
        """checks if the users exists"""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def check_pin(self, user: User, user_pin: str) -> bool:
        """checks if the user's pin is correct"""
        return user.check_pin(user_pin)

    def get_user_balance(self, user: User) -> int:
        """give the balance of the current user"""
        return user.balance

    def change_balance(self, user: User, new_balance):
        """changes the balance of the current user"""
        if new_balance < 0:
            print('Cannot update balance. Reason: New balance is negative')
            return

        user.balance = new_balance
        self.save_users()

    def upload_money(self, user: User, amount: int):
        """adds the amount to the balance of current user"""
        if amount <= 0:
            print('You must upload more than 0')
            return

        new_balance = user.balance + amount
        self.change_balance(user, new_balance)

    def withdrawal_money(self, user: User, amount: int):
        """takes the amount from the balance of current user"""
        if amount <= 0:
            print('You must withdrawal more than 0')
            return
        if user.balance < amount:
            print('You want to withdrawal more than you have')
            return

        new_balance = user.balance - amount
        self.change_balance(user, new_balance)

    def show_balance(self, user: User):
        """shows the user's current balance"""
        print(f"You choosed the Show balance operation!\n"
              f"Your current balance is {user.balance}")

    def save_users(self):
        """loads all information about users"""
        with open("database.txt", "w") as f:
            for user in self.users:
                f.write(f"{user.user_id}:{user.pin}:{user.balance}\n")

    def change_user_pin(self, user: User):
        """changes the user's pin"""
        count_attempts_pin = 1
        while count_attempts_pin <= 3:
            user_pin = input("Enter your PASS: ")
            access = user.check_pin(user_pin)
            if not access:
                print(f"Wrong PASS. {count_attempts_pin}/3. Try again")
                count_attempts_pin += 1
                continue
            else:
                new_pin = input("Enter NEW PASS: ")
                break

        if access:
            user.pin = new_pin
            self.save_users()
        else:
            print("Try next time. Too much fails")

