#           Polynomial Evaluation
# Write a Python program that prompts the user
# to enter the coefficients of a polynomial
# function of degree n. Then, ask the user to enter
# a value for x. The program should evaluate the
# polynomial at the given value of x and display the result.
# Ensure that your program can handle polynomials of any degree.


def evaluate_polynomial(coefficients, x):
    result = 0

    for i in range(len(coefficients)):
        result += coefficients[i] * (x ** i)

    return result

def main():
    print("Polynomial Evaluator")
    print("--------------------")

    try:
        degree = int(input("Enter the degree of the polynomial: "))

        coefficients = []
        for i in range(degree + 1):
            coefficient = float(input(f"Enter the coefficient of x^{i}: "))
            coefficients.append(coefficient)

        x = float(input("Enter the value of x: "))

        result = evaluate_polynomial(coefficients, x)
        print("The result of the polynomial evaluation is:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()


