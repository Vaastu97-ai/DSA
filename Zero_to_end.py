def Zero_to_end(arr):
    j = 0

    for i in range (len(arr)):

        if arr[i] !=0:
            arr[i] , arr[j] = arr[j] , arr[i]
            j += 1
        return arr
    
arr = list(map(int , input("Enter the numbers:").split()))

print(arr)

print("Array after moving the zero to end:",Zero_to_end(arr))

    