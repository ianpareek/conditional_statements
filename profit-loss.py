actual_cost = float(input("Please enter the acual price of the item"))
sale_amount = float(input("Please enter the sale price of the item"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit", amount)

else:
    amount = actual_cost - sale_amount
    print("Total Loss", amount)
