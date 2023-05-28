#       Integration Approximation
# Write a Python program that calculates
# the approximate value of a definite
# integral using the midpoint rule.
# Prompt the user to enter the lower
# and upper limits of integration,
# as well as the number of subintervals (n)
# to divide the interval into.
# The program should display the approximate value
# of the integral using the midpoint rule formula:

# ∫[a, b] f(x) dx ≈ h * (f(x₁ + h/2) + f(x₂ + h/2) + ... + f(xₙ + h/2))

# where h = (b - a) / n and xᵢ = a + (i - 0.5) * h for i = 1, 2, ..., n.


def approximate_integral(f, a, b, n):
    h = (b - a) / n  # Width of each subinterval
    total_sum = 0

    for i in range(n):
        x_i = a + (i + 0.5) * h  # Midpoint of the current subinterval
        total_sum += f(x_i)

    integral_approximation = h * total_sum
    return integral_approximation

def main():
    print("Approximate Integral Calculator (Midpoint Rule)")
    print("----------------------------------------------")

    try:
        # Get user input
        a = float(input("Enter the lower limit of integration (a): "))
        b = float(input("Enter the upper limit of integration (b): "))
        n = int(input("Enter the number of subintervals (n): "))

        # Define the function to integrate
        def f(x):
            return x**2  # Replace with your desired function

        # Calculate the approximate integral
        approximation = approximate_integral(f, a, b, n)

        # Display the result
        print("The approximate value of the definite integral is:", approximation)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

