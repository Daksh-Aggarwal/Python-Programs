amt = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the duration (in years): "))

simple_interest = (amt * rate * time)/100

print(f"The simple interest is {simple_interest}.")