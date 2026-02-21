#sorting array
def sort(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True
#count the occurence
def occurence(arr , target):
    count=0
    for i in arr:
        if i == target:
            count += 1
        return count
#max number
def max_num(arr):
    if not arr:
        return None
    
    max = arr[0]
    for num in arr:
      if num > max:
        max = num
    return max
#min number
def min_num(arr):
    if not arr:
        return None
    min = arr[0]
    for num in arr:
        if num < min:
            min= num
    return min

