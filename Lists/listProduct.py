size = int(input("How many elements do you want to enter? "))
l = []
product = 1

for i in range(size):
    l.append(int(input("Enter the element: ")))
    product *= l[i]

print(f"Product of the elements in the list is {product}.")