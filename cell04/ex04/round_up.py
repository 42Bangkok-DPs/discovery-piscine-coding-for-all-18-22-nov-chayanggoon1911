import math
number = input("Give me a number: ")
try:
    num = float(number)
    rounded_up = math.ceil(num)
    print(rounded_up)
except ValueError:
    print("Invalid input. Please enter a valid number.")
