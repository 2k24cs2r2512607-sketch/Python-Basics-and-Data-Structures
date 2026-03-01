# Factorial of a number
num = int(input("Enter Number:"))
fact = 1
if num < 0:
    print("Factorial cannot be defined for negative numbers")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial =", fact)
