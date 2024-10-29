size = int(input("How many elements do you want to enter? "))
l = []

for i in range(size):
    l.append(int(input("Enter the element: ")))

# Length = size but trying out the in-built function
print(f"Length of the list is {len(l)}.")