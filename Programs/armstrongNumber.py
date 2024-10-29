num = int(input("Enter the number: "))
digits = 0
sum = 0
temp = num

while num > 0:
    digits += 1
    num //= 10

num = temp

while num > 0:
    digit = num % 10
    print(digit)
    sum += digit**digits
    num //= 10

num = temp

if sum == num:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")