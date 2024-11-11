# Prompts user for password until triggers a log in or lockout
Attempts = 0
password = ""
Correctpassword = "hello"
while Attempts < 3:
    password = input("Enter a password: ")
    if password == Correctpassword:
        print("log in")
        break
    else:
        Attempts += 1
        if Attempts == 3:
            print("Too many attempts")