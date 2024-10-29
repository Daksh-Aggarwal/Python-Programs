num = int(input("Enter the number: "))

for i in range(1, num):
    print(f"TABLE OF {i}")
    for j in range(1, 11):
        print(f"{j} x {i} = {j * i}")
    print()