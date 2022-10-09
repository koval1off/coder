from cryptography.fernet import Fernet


class User:
    def __init__(self, user_id: str, pin: str, balance: int):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

    def _get_key(self) -> bytes:
        with open("mykey.key", "rb") as file:
            key = file.read()
        return key

    def check_pin(self, user_pin: str) -> bool:
        return user_pin == self.decrypt_pin(self.pin)

    def encrypt_pin(self, user_pin: str) -> str:
        key = self._get_key()
        fernet = Fernet(key)
        encrypt_pin = fernet.encrypt(user_pin.encode())
        return encrypt_pin.decode()

    def decrypt_pin(self, user_pin) -> bool:
        key = self._get_key()
        fernet = Fernet(key)
        decrypt_user_pin = fernet.decrypt(user_pin).decode()
        return decrypt_user_pin

