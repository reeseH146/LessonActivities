UserNameList = []

def existingUsers(NewUName, UNameList):
    for UserNames in UNameList:
        if UserNames == NewUName: # If name found in list then returns early
            return False
    return True # Always returns true if there is not false since return terminates the function

while True:
    #Asks for employee details
    FirstName = "REESE"
    SecondName = "HE"

    # Creates the username
    Unique = False
    Number = 1
    while not Unique:
        Username = f"{SecondName}{FirstName[0]}{Number}"
        Unique = existingUsers(Username, UserNameList)
        if Unique: # Breaks the loop
            print(f"Your username is : {Username}\n")
            UserNameList.append(Username)
        elif not Unique: # Continues the loop
            print(f"Username {Username} not unique.")
            Number += 1

    # Continues the function
    Continue = input("Continue? : Y/N : ")
    if Continue != "Y":
        break