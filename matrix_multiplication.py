#           Matrix Multiplication
# Write a Python program that prompts the user
# to enter two matrices as input.
# Then, perform matrix multiplication on the
# input matrices and display the resulting matrix.
# Make sure to handle cases where the matrices are
# incompatible for multiplication and provide appropriate error messages.

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Error: Matrices are incompatible for multiplication.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def get_matrix_from_input(rows, cols):
    matrix = []

    for i in range(rows):
        row = input(f"Enter space-separated values for row {i+1}: ").split()
        if len(row) != cols:
            raise ValueError("Error: Invalid number of elements in a row.")
        matrix.append([float(num) for num in row])

    return matrix

def main():
    print("Matrix Multiplication")
    print("---------------------")

    try:
        rows1 = int(input("Enter the number of rows for the first matrix: "))
        cols1 = int(input("Enter the number of columns for the first matrix: "))
        matrix1 = get_matrix_from_input(rows1, cols1)

        rows2 = int(input("Enter the number of rows for the second matrix: "))
        cols2 = int(input("Enter the number of columns for the second matrix: "))
        matrix2 = get_matrix_from_input(rows2, cols2)

        result = multiply_matrices(matrix1, matrix2)

        print("The result of matrix multiplication is:")
        for row in result:
            print(*row)

    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
