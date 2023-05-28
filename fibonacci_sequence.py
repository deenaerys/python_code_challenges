#               Fibonacci Sequence
# Write a Python program that prompts the user
# to enter a positive integer n and generates
# the first n terms of the Fibonacci sequence.
# The Fibonacci sequence is defined as follows:
# the first two terms are 0 and 1, and each
# subsequent term is the sum of the two
# preceding terms. Display the resulting
# sequence in a comma-separated format.

def generate_fibonacci_sequence(n):
    sequence = [0, 1]

    if n == 1:
        return sequence[:1]
    elif n == 2:
        return sequence

    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

def main():
    print("Fibonacci Sequence Generator")
    print("---------------------------")

    try:
        n = int(input("Enter a positive integer: "))

        if n <= 0:
            print("Invalid input. Please enter a positive integer.")
            return

        fibonacci_sequence = generate_fibonacci_sequence(n)

        print("The Fibonacci sequence of length", n, "is:")
        print(*fibonacci_sequence, sep=", ")

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
