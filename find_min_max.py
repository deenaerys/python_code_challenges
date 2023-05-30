def find_min_max(numbers):
    if not numbers:
        return None

    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num


n=int(input("Enter number of elements: "))

numbers_list=[]

for i in range(n):
    x=int(input())
    numbers_list.append(x)
result=find_min_max(numbers_list)
print("The numbers are:",numbers_list)

if result is not None:
    min_num, max_num = result
    print(f"Minimum number: {min_num}")
    print(f"Maximum number: {max_num}")
else:
    print("Empty list provided.")


