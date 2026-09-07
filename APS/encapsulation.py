class Account:
    def __init__(self, account_number, pin):
        self.__account_number = account_number
        self.__pin = pin

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must contain exactly 4 digits.")

    def __str__(self):
        return "Account Number: " + self.__account_number + ", PIN: ****"

account = Account("123456789", "1234")
print(account)
account.set_pin("5678")
account.set_pin("123")
print(account)