accounts = {}
class Transactions(object):
    def deposit(self,password):
        print("How much money would you like to deposit into your account?")
        moneyDeposit = int(input("Please enter your amount here: "))
        accounts[password] += moneyDeposit
        print("You have succesfully deposited ",moneyDeposit," dollars")
        print("You now have ",accounts[password]," dollars in your account!")
        print("Redirecting Home!")
        EnteringBank().accountVerify()
    def withdraw(self,password):
        print("How much money would you like to withdraw from your account?")
        moneyWithdraw = int(input("Enter the amount here: "))
        if accounts[password] >= moneyWithdraw:
            accounts[password] -= moneyWithdraw
            print("You now have ",accounts[password]," dollars in your account!")
            print("Redirecting home....")
            EnteringBank().accountVerify()
        else:
            print("Your account does not have that much money in it. Redirecting Home.....")

class EnteringBank(object):
    def accountVerify(self):
        print("Hello and Welcome to the Bank!")
        print("Do you have an account? Type 1 if yes, else, type 2")
        ask = int(input("Do you have an account: "))
        if ask == 1:
            print("Redirecting:")
            self.askPassword()
        else:
            if ask == 2:
                print("Redirecting....")
                account().create()
            else:
                quit(EnteringBank())
    def askPassword(self):
        password = int(input("Please enter your password here: "))
        if password in accounts:
            print("Password correct! What would you like to do next?")
            print("Type 1 to deposit.")
            print("Type 2 to withdraw.")
            print("Type 3 to delete your account.")
            choice = int(input("Please enter your choice here: "))
            if choice == 1:
                Transactions().deposit(password)
            else:
                if choice == 2:
                    Transactions().withdraw(password)
                else:
                    account().delete(password)
        else:
            print("Password incorrect or not found. Make sure you have created an account. Redirecting to home....")
            self.accountVerify()
class account(object):
    def create(self):
        print("Hello! Lets create your account!")
        passwordCreate = int(input("Please enter your password made entirely of numbers here: "))
        accounts[passwordCreate] = 0
        print("Your account has been created. Thank you! Redirecting to home.....")
        EnteringBank().accountVerify()
    def delete(self, password):
        shouldDelete = int(input("To delete your account type 1, else type 2: "))
        if shouldDelete == 1:
            del(accounts[password])
            print("Your account has been deleted. Redirecting home...")
            EnteringBank().accountVerify()
        else:
            print("Your account has not been deleted. Redirecting home....")
            EnteringBank().accountVerify()



EnteringBank().accountVerify()