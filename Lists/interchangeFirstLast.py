size = int(input("How many numbers do you want to enter? "))
l = []

for i in range(size):
    l.append(input("Enter the number: "))

print("Here's the entered list: ")
print(l)

l[0], l[-1] = l[-1], l[0]

print("Here's the list with interchanged first and last elements: ")
print(l)