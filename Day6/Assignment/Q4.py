#Write a program using short-circuit evaluation with 'and' to check if a person is eligible to vote: age >= 18 AND is_citizen is True AND is_registered is True. Print the result without calling any unnecessary checks


age = int(input("Enter Your age: "))
is_citizen =True
is_registered = True

if age >= 18 and is_citizen and is_registered:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")
