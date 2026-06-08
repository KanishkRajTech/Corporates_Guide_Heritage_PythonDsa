#Using match-case, write a program that takes a day number (1-7) as input and prints the corresponding day name (1=Monday ... 7=Sunday). Handle invalid inputs with a default case.


day_number = int(input("Enter the day number: "))

if day_number ==1:
    print("Monday")
elif day_number ==2:
    print("Tuesday")
elif day_number ==3:
    print("Wednesday")
elif day_number ==4:
    print("Thursday")
elif day_number ==5:
    print("Friday")
elif day_number ==6:
    print("Saturday")
elif day_number ==7:
    print("Sunday")
else:
    print("Invalid day number")