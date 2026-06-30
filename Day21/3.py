numbers = [1, 2, 3, 2, 4, 5, 1, 6]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:")
print(unique)