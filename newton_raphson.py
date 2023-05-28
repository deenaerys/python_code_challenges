#           Newton-Raphson Method 
# Write a Python program that implements
# the Newton-Raphson method to find the
# root of a given equation.
# Prompt the user to enter the equation,
# the initial guess for the root,
# and the maximum number of iterations.
# The program should iteratively calculate the root using the formula:
# xᵢ₊₁ = xᵢ - f(xᵢ) / f'(xᵢ)
# where f(x) is the equation and f'(x) is the derivative of the equation.
# Display the final approximation of the root after the specified number
# of iterations or if the approximation converges within a certain tolerance.


from sympy import symbols, diff, sympify

def newton_raphson(equation, x, max_iterations, tolerance):
    f = sympify(equation)
    df = diff(f)

    for i in range(max_iterations):
        f_value = f.subs(x, x_value)
        df_value = df.subs(x, x_value)

        if abs(f_value) < tolerance:
            break

        x_value = x_value - f_value / df_value

    return x_value

def main():
    print("Newton-Raphson Method")
    print("---------------------")

    try:
        equation = input("Enter the equation: ")
        x = symbols('x')
        x_value = float(input("Enter the initial guess for the root: "))
        max_iterations = int(input("Enter the maximum number of iterations: "))
        tolerance = float(input("Enter the tolerance: "))

        root = newton_raphson(equation, x, max_iterations, tolerance)
        print("The approximation of the root is:", root)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
