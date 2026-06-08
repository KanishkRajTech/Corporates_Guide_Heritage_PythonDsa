product = input("Enter a product name: ")
quantity = int(input("Enter a quantity: "))
price= int(input("Enter a price: "))
total_cost =quantity *price
gst =total_cost*0.18
final_bill =total_cost+gst

print("Total Cost",total_cost)
print("GST",gst)
print("Final Bill",final_bill)