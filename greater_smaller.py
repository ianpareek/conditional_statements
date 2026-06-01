comparision_number = 15
input_number = int(input("Enter a number:"))

if input_number > comparision_number:
    print("The number is greater than 15")
    print("I am in if block")
elif input_number < comparision_number:
    print("The number is smaller than 15")
    print("I am in elif block")
else:
    print("The number is 15 itself")
    print("I am in else block")