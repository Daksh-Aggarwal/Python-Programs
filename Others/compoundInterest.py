amt = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the duration (in years): "))

compound_interest = amt - (amt * (1 - (rate/100))**time)

print(f"The compound interest is {compound_interest}.")