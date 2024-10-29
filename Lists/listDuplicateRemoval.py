size = int(input("How many elements do you want to enter? "))
l = []

for i in range(size):
    l.append(int(input("Enter the element: ")))

# Sets don't allow duplicates
print(list(set(l)))
