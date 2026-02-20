def rep_num(arr , target):
    count = 0

    for num in arr :
        if num == target:
            count +=1
    return count
    
arr = list(map(int , input("Enter the numbers:").split()))
target = int(input("Enter the target:"))

print(rep_num(arr , target))
