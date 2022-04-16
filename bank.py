class ATM:
    def __init__(self):
        self.user_balance = 5000

    def change_balance(self, new_balance):
        if new_balance < 0:
            print('Cannot update balance. Reason: New balance is negative')
            return

        self.user_balance = new_balance

    def upload_money(self, amount):
        if amount <= 0:
            print('You must upload more than 0')
            return

        new_balance = self.user_balance + amount

        self.change_balance(new_balance)

    def withdrawal_money(self, amount):
        if amount <= 0:
            print('You must withdrawal more than 0')
            return

        if self.user_balance < amount:
            print('You want to withdrawal more than you have')
            return

        new_balance = self.user_balance - amount
        self.change_balance(new_balance)

    def show_balance(self):
        print(f"You choosed the Show balance operation!\n"
              f"Your current balance is {self.user_balance}")
