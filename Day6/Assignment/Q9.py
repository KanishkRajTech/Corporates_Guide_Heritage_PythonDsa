# Build a complete ATM system using if-elif-else and nested if. Features: (1) PIN verification, (2) Check balance, (3) Withdraw (check sufficient funds), (4) Deposit. Use match-case for menu selection.


balance = 10000
pin = 1234
pin = int(input("Enter your PIN: "))
option = int(input("Enter your option: "))

if pin == 1234:
    print("PIN verified")
    if option == 1:
        print("Balance: ", balance)
    elif option == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("available Balance: ", balance)
    elif option == 3:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful")
        print("available Balance: ", balance)
    else:
        print("Invalid option")
else:
    print("Invalid PIN")    


