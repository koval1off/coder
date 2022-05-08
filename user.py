class User:
    def __init__(self, user_id: str, pin: str, balance: int):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

    def check_pin(self, user_pin: str) -> bool:
        return self.pin == user_pin

