import logging
import threading

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BankAccount:

    def __init__(self, balance=0, currency="CAD"):
        self.balance = balance
        self.currency = currency
        logging.info(f"Account created with balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            logging.error("Deposit amount must be positive")
            return
        self.balance += amount
        logging.info(f"Deposited {amount}, new balance is {self.currency} {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            logging.error("Withdrawal amount must be positive")
            return
        if amount > self.balance:
            logging.error("Insufficient funds")
            return
        self.balance -= amount
        logging.info(f"Withdrew {amount}, new balance is CAD${self.balance}")

    def timed_withdraw(self, amount, timeout):
        def perform_withdraw():
            self.withdraw(amount)

        timer = threading.Timer(timeout, perform_withdraw)
        timer.start()


# Example usage
bank_account = BankAccount(1000, "USD")
bank_account.deposit(50)
bank_account.withdraw(30)
bank_account.timed_withdraw(20, 5)  # Withdraw 20 after a 5-second delay
bank_account.withdraw(-30)
