size = int(input("How many elements do you want to enter? "))
l = []

for i in range(size):
    l.append(input("Enter the element: "))

l_rev = l[::-1]

print("Here's the entered list: ")
print(l)

print("Here's the reversed list: ")
print(l_rev)