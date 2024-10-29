while True:

    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    operation = input("Which operation do you want to perform (+, -, *, /, //, %, **)? ")

    if operation == '+':
        result = num_1 + num_2
        print(f"The sum is {result}.")

    elif operation == '-':
        result = num_1 - num_2
        print(f"The difference is {result}.")

    elif operation == '*':
        result = num_1 * num_2
        print(f"The product is {result}.")

    elif operation == '/':
        result = num_1 / num_2
        print(f"The result is {result}.")

    elif operation == '//':
        result = num_1 // num_2
        print(f"The result is {result}.")

    elif operation == '%':
        result = num_1 % num_2
        print(f"The result is {result}.")

    elif operation == '**':
        result = num_1 ** num_2
        print(f"The result is {result}.")

    else:
        print("Invalid operator! Try again.")

    cont = input("Do you wish to use the calculator again (Y/N)? ")
    if cont == 'Y' or cont == 'y':
        continue
    elif cont == 'N' or cont == 'n':
        print("Thanks for using the calculator.")
        break
    else:
        print("Invalid input! Terminating.")
        break