def max_num(arr):
    max = arr[0]

    for num in arr:
        if num > max:
            max = num
    return max

arr = list(map(int, input("Enter the numbers :").split()))
print(arr)

print(max_num(arr))
