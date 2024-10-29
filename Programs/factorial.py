num = int(input("Enter the number: "))
result = 1
i = num

while i > 0:
    result *= i
    i -= 1

print(f"Factorial of {num} is {result}.")