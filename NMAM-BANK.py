class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}. \nNew balance: ₹{self.balance}.")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}. \nNew balance: ₹{self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")


    def get_balance(self):
        return self.balance


    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ₹{self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.bank_name = "NMAM BANK"


    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            new_account = Account(account_number, account_holder)
            self.accounts[account_number] = new_account
            print(f"✅ Account created for {account_holder} at {self.bank_name}.")
        else:
            print(f"❌ Account {account_number} already exists in {self.bank_name}.")


    def deposit(self, account_number, amount):
        self.accounts[account_number].deposit(amount)


    def withdraw(self, account_number, amount):
        self.accounts[account_number].withdraw(amount)


    def check_balance(self, account_number):
        balance = self.accounts[account_number].get_balance()
        print(f"Balance for account {account_number}: ₹{balance}.")


    def display_accounts(self):
        if self.accounts:
            print(f"Accounts in {self.bank_name}:")
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts in the bank.")

def banner():
    TITLE = "\033[38;2;135;206;235m"   # hex #000042 (dark blue)
    ACCENT = "\033[255;255;255;255;255m"  # hex #000042 (dark blue)
    RESET = "\033[0m"


    print(TITLE + r"""
███╗   ██╗███╗   ███╗ █████╗ ███╗   ███╗    ██████╗  █████╗ ███╗   ██╗██╗  ██╗
████╗  ██║████╗ ████║██╔══██╗████╗ ████║    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██╔██╗ ██║██╔████╔██║███████║██╔████╔██║    ██████╔╝███████║██╔██╗ ██║█████╔╝ 
██║╚██╗██║██║╚██╔╝██║██╔══██║██║╚██╔╝██║    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║    ██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    """ + RESET)
    print(ACCENT + "======================== Always at your Service 🏦 ===========================\n" + RESET)



def main():
    bank = Bank()


    while True:
        banner()
        print(f"\n             🏦 {bank.bank_name} 🏦")
        print("=" * 40)
        print("          Bank Management System")
        print("=" * 40)
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")
        print("=" * 40)


        choice = input("Enter your choice: ")


        if choice == '1':
            account_number = input("Enter account number: ")
            if account_number in bank.accounts:
                print(f"❌ Account {account_number} already exists in {bank.bank_name}.")
                continue
            account_holder = input("Enter account holder name: ")
            bank.create_account(account_number, account_holder)
        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number not in bank.accounts:
                print(f"❌ Invalid account number. Account {account_number} not found in {bank.bank_name}.")
                continue
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number not in bank.accounts:
                print(f"❌ Invalid account number. Account {account_number} not found in {bank.bank_name}.")
                continue
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number not in bank.accounts:
                print(f"❌ Invalid account number. Account {account_number} not found in {bank.bank_name}.")
                continue
            bank.check_balance(account_number)
        elif choice == '5':
            bank.display_accounts()
        elif choice == '6':
            print(f"\n🙏 Thank you for visiting {bank.bank_name} 🙏")
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
