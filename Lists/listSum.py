size = int(input("How many elements do you want to enter? "))
l = []

for i in range(size):
    l.append(int(input("Enter the element: ")))

print("Here's the entered list: ")
print(l)

print(f"Sum of the elements in the list is {sum(l)}.")