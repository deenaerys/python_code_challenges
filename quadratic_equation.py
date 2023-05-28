#           Quadratic Equation Solver
# Write a Python program that prompts the user
# to enter the coefficients (a, b, c) of a quadratic
# equation (ax^2 + bx + c = 0) and 
# calculates and displays the roots of the equation. 
# Your program should handle cases where the equation
# has no real roots, one real root, or two real roots.
# Ensure that you handle any division by zero errors
# and provide appropriate error messages if necessary.

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return None

def main():
    print("Quadratic Equation Solver")
    print("-------------------------")

    try:
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))

        roots = solve_quadratic_equation(a, b, c)

        if roots is None:
            print("The equation has no real roots.")
        elif isinstance(roots, tuple):
            root1, root2 = roots
            print("The equation has two real roots:")
            print("Root 1:", root1)
            print("Root 2:", root2)
        else:
            root = roots
            print("The equation has one real root:")
            print("Root:", root)

    except ValueError:
        print("Invalid input. Please enter numeric coefficients.")

if __name__ == "__main__":
    main()
