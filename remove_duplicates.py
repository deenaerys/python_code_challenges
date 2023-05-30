def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

n=int(input("Enter number of elements: "))
input_list=[]
for i in range(n):
    x=int(input())
    input_list.append(x)
result=remove_duplicates(input_list)

print("Original list:", input_list)
print("List with duplicates removed:", result)
