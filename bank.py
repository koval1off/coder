from dataclasses import dataclass
from user import User
from typing import Optional
import mysql.connector


class ATM:
    def __init__(self):
        self.users = self._read_users()

    def _read_users(self) -> list:
        """reads database and writes users"""
        users = []
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kovalsql#12345",
            database="testdatabase"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users")
        data_users = mycursor.fetchall()
        
        for data in data_users:
            user = User(data[0],
                        data[1],
                        data[2])
            users.append(user)
        return users

    def print_users(self) -> None:
        """prints users' info"""
        for user in self.users:
            print(f"User_ID: {user.user_id}; User_PIN: {user.pin}; User_BALANCE: {user.balance}")

    def get_user(self, user_id: str) -> Optional[User]:
        """
        checks if the users exists

        :param user_id: The id of user
        :return: user if exists or None
        """

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

    def change_balance(self, user: User, new_balance: int) -> None:
        """changes the balance of the current user"""
        if new_balance < 0:
            print('Cannot update balance. Reason: New balance is negative')
            return

        user.balance = new_balance
        self.save_users(user)

    def upload_money(self, user: User, amount: int) -> None:
        """adds the amount to the balance of current user"""
        if amount <= 0:
            print('You must upload more than 0')
            return

        new_balance = user.balance + amount
        self.change_balance(user, new_balance)

    def withdrawal_money(self, user: User, amount: int) -> None:
        """takes the amount from the balance of current user"""
        if amount <= 0:
            print('You must withdrawal more than 0')
            return
        if user.balance < amount:
            print('You want to withdrawal more than you have')
            return

        new_balance = user.balance - amount
        self.change_balance(user, new_balance)

    def show_balance(self, user: User) -> None:
        """shows the user's current balance"""
        print(f"You choose the Show balance operation!\n"
              f"Your current balance is {user.balance}")

    def change_user_pin(self, user: User, new_pin: str) -> None:
        """changes the user's pin"""
        if not new_pin:
            return

        user.pin = user.encrypt_pin(new_pin)
        self.save_users(user)

    def save_users(self, user: User) -> None:
        """loads all information about users in database"""
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kovalsql#12345",
            database="testdatabase"
        )

        mycursor = mydb.cursor()
        mycursor.execute("UPDATE users SET pin = %s, balance = %s WHERE user_id = %s", (user.pin, user.balance, user.user_id))
        mydb.commit()
