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
