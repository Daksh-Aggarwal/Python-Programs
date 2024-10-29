size = int(input("How many numbers do you want to enter? "))
l = []

for i in range(size):
    l.append(input("Enter the number: "))

print(f"The largest number in the entered list is {max(l)}.")
print(f"The smallest number in the entered list is {min(l)}.")