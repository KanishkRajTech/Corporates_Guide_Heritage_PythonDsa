arr = [12, 45, 7, 89, 23]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest =", largest)
print("Smallest =", smallest)