def leader(arr):
    result = []
    max_right = float('-inf')

    for i in range(len(arr) -1 , -1 ,-1):
        
        if arr[i] > max_right:
            result.append(arr[i])
            max_right = arr[i]
    
    result.reverse()
    
    return result

arr = list(map(int , input("Enter the numbers :").split()))

print ("the entered array is :" , arr)

print("The Leaders of teh array are:" , leader(arr))