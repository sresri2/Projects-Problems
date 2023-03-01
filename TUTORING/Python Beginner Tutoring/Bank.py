passwordDict = {
    "Bob": 12345,
    "Jeff": 2310
}
accountsDict = {
    "Bob": 1000,
    "Jeff": 2000
}
def editAccounts(account):
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
def login():
    username = input("Enter username: ")
    password = int(input("Enter Password: "))

    if username in passwordDict:
        if password == passwordDict[username]:
            print("You are logged in.")
            editAccounts(username)


        else:
            print("Password you entered is wrong.")
    else:
        print("Username not found.")

login()








