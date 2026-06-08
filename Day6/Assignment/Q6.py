# Write a program that uses short-circuit evaluation with 'or' to provide a default username. If a user enters an empty string for username, default to 'Guest' without using an if statement directly — use the 'or' operator.

user_name = input("Enter user name: ")
default_user = "guest"

final_user = user_name or default_user
print("Hello",final_user)