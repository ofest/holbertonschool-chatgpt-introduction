class Checkbook:
    """
    A simple Checkbook class to handle deposits, withdrawals, and balance inquiries.
    """

    def __init__(self):
        """Initialize a checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
        amount (float): The amount of money to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.

        Parameters:
        amount (float): The amount of money to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def get_float_input(prompt):
    """
    Get a valid float input from the user, with error handling.

    Parameters:
    prompt (str): The message shown to the user.

    Returns:
    float: A valid float entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """
    Main function to interact with the Checkbook.
    Supports deposit, withdraw, balance inquiry, and exit.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Exiting. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_float_input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_float_input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
    