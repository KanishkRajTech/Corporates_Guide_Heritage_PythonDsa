# Write a nested if program for a cinema ticket price system: Adults (>=18) pay 200, but Seniors (>=60) pay 100. Children (<18) pay 80, but children under 5 enter free. Add a group discount: if group size > 10, apply 20% off the total.


age = int(input("Enter age: "))
group_size = int(input("Enter group size: "))


if age >= 18:
    if age >= 60:
        price = 100
        print("Senior Citizen Ticket: ₹100")
    else:
        price = 200
        print("Adult Ticket: ₹200")
else:
    if age < 5:
        price = 0
        print("Child under 5: Free Entry")
    else:
        price = 80
        print("Child Ticket: ₹80")

total = price * group_size

if group_size > 10:
    total = total * 0.8
    print("Group Discount Applied: 20%")

print("Total Amount: ₹", total)