accounts = {}
done = False

class account(object):
    def create(self):
        print("Hello! Lets create your account!")
        passwordCreate = int(input("Please enter your password made entirely of numbers here: "))
        accounts[passwordCreate] = 0
        print("Your account has been created. Thank you! Redirecting to home.....")
        return
    def delete(self, password):
        shouldDelete = int(input("To delete your account type 1, else type 2: "))
        if shouldDelete == 1:
            del(accounts[password])
            print("Your account has been deleted. Redirecting home...")
        else:
            print("Your account has not been deleted. Redirecting home....")
        return
class Bank(object):
    quitting = False
    firstTime = True
    def Controller(self):
        if self.firstTime:
            print("Hello and Welcome to the Bank! Do you have an account?")
            self.firstTime = False
        accountOrNot = int(input("Enter 1 if you have an account, else enter 2. Enter 3 to leave the Bank: "))
        if accountOrNot == 2:
            account().create()
            password = self.askPassword()
            if password != "Wrong":
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
                print("Wrong Password!")
        else:
            if accountOrNot == 1:
                password = self.askPassword()
                if password != "Wrong":
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
                    print("Wrong Password!")
                    self.quitting = True
            else:
                self.quitting = True
        if self.quitting == True:    
            print("Thank you for visiting the Bank!")

        
    def askPassword(self):
        password = int(input("Please enter your password here: "))
        if password in accounts:

            return password
        else:
            return "Wrong"
class Transactions(object):
    def deposit(self,password):
        print("How much money would you like to deposit into your account?")
        moneyDeposit = int(input("Please enter your amount here: "))
        accounts[password] += moneyDeposit
        print("You have succesfully deposited ",moneyDeposit," dollars")
        print("You now have ",accounts[password]," dollars in your account!")
        print("Redirecting Home!")
        return
    def withdraw(self,password):
        print("How much money would you like to withdraw from your account?")
        moneyWithdraw = int(input("Enter the amount here: "))
        if accounts[password] >= moneyWithdraw:
            accounts[password] -= moneyWithdraw
            print("You now have ",accounts[password]," dollars in your account!")
            print("Redirecting home....")
        else:
            print("Your account does not have that much money in it. Redirecting Home.....")
        return

while not done:
    enterBank = int(input("Enter 1 to Enter the Bank, and enter 2 to Leave: "))
    if enterBank == 1:
        Bank().Controller()
    else:
        quit()

