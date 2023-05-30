def calculate_even_sum(n):
    total_sum = 0
    numbers=[]
    for num in range(2, n+1,2):
        total_sum += num
        numbers.append(num)
    print("The numbers are",numbers)
    return total_sum

# Test the function
number = int(input("Enter a number: "))
result = calculate_even_sum(number)
print(f"The sum of even numbers between 1 and {number} is: {result}")
