num = int(input("Enter the number: "))
sum = 0

for i in range(1, num + 1):
    sum += i**3

print(f"Sum of cubes of first {num} natural numbers is {sum}.")