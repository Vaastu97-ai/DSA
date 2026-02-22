def sec_large(arr):
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        
        elif num != largest and num > second_largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

arr = list(map(int , input("Enter the numbers :").split()))

print(arr)
print("Second largest number is :" ,sec_large(arr))
