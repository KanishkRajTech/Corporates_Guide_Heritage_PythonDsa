# Build a simple login system using nested if statements. Check: (1) username exists, (2) account is active, (3) password matches. Print appropriate messages for each failure case.


user_name = "Kanishkraj"
password = "raj123"
actount_active = True

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == user_name:
    if actount_active == True:
        if password == password:
            print("Login Sucessfull")
        else:
            print("Invalid Password")
    else:
        print("Account is not active")
else:
    print("Username not found")