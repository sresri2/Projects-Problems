
accountsDict = {
    "Bob": 1000,
    "Jeff": 2000
}
def editAccounts():
    account = input("Which account do you want to open: ")
    if account in accountsDict:
        addOrRemove = int(input("Do you want to add or remove money? Type 1 to add, 2 to remove: "))
        if addOrRemove == 1:
            change = int(input("How much money do you want to add: "))
            accountsDict[account] += change
            print(accountsDict[account])
        else:
            change = int(input("How much money do you want to remove: "))
            if change > accountsDict[account]:
                print("You do not have this much money in your account to remove.")
                quit()
            accountsDict[account] -= change
            print(accountsDict[account])
    else:
        print("Account does not exist.")
        
editAccounts()




    

