

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print("Addition",num1+num2)
print("Subtraction",num1-num2)
print("Multiplication",num1*num2)
print("Division",num1/num2)


# Shopping Bill Generator
# Take:
# Product Name
# Quantity
# Price
# Calculate:
# Total Cost
# GST (18%)
# Final Bill
# This is bonus question

product = input("Enter a product name: ")
quantity = int(input("Enter a quantity: "))
price = int(input("Enter a price: "))
total_cost = quantity *price
gst =total_cost * 0.18
final_bill = total_cost+gst

print("Total Cost",total_cost)
print("GST",gst)
print("Final Bill",final_bill)