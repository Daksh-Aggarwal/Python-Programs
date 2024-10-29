size = int(input("How many elements do you want to enter? "))
l = []

for i in range(size):
    l.append(input("Enter the element: "))

print("Here's the entered list: ")
print(l)

index_1 = int(input("Index 1? "))
index_2 = int(input("Index 2? "))

temp = l[index_1]
l[index_1] = l[index_2]
l[index_2] = temp

print("Here's the formatted list: ")
print(l)