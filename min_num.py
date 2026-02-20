def min_num(arr):
    min = arr[0]

    for num in arr:
        if num < min:
            min = num
    return min

arr = list(map(int , input("enter the numbers :").split()))
print(arr)

print(min_num(arr))