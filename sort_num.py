def sort(arr):
    for i in range(len(arr) -1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = list(map(int , input("Enter the numbers :").split()))

if sort(arr):
    print("array is sorted")
    print(arr)
    print(sorted(arr))
else:
    print("array is not sorted")
    print(arr)
