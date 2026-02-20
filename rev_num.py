def rev_arr(arr):
   left = 0
   right = len(arr) - 1

   while left < right :
      arr[left] , arr[right] = arr[right] , arr[left]
      left +=1
      right-=1
   return arr

arr = list(map(int , input("enter the numbers :").split()))
print(arr)
print(rev_arr(arr))