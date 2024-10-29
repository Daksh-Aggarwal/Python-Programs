print("Ensure that your equation is of the form ax² + bx + c = 0.")
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

d = (b**2)  - (4 * a * c)

if d < 0:
    print("The given equation does not have any real roots.")
else:
    soln_1 = (-b + (d**0.5))/(2 * a)
    soln_2 = (-b - (d**0.5))/(2 * a)

    print(f"The two solutions to the given quadratic equation are {soln_1} and {soln_2}.")