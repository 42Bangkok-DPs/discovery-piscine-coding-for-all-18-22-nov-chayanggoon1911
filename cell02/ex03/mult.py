number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = number1 * number2

if result > 0:
    print(f"The result is positive.")
elif result < 0:
    print(f"The result is negative.")
else:
    print(f"The result is positive and negative.")

print(f"{number1} * {number2} = {result}")
