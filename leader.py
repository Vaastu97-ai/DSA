def leader(arr):
    result = []
    max_right = float('-inf')

    for i in range(len(arr) -1 , -1 ,-1):
        
        if arr[i] > max_right:
            result.append(arr[i])
            max_right = arr[i]
    
    result.reverse()
    
    return result

