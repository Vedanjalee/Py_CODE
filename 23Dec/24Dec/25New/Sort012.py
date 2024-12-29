def sort_012(arr):

   n = len(arr)
   low = 0
   high = n-1 
   mid = 0 

   while mid<= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1

        elif arr[mid] == 1:
            mid = mid + 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
   return arr     

arr =[0,1,2,0,1,2]
arr = sort_012(arr) 

for i in arr:
    print(i, end =" ")

            
