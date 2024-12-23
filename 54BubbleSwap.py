arr = [64, 34, 25, 12, 22, 11, 90]
# arr=[11, 1, 22, 25, 34, 64, 90]
n = len(arr)
swap_count = 0

for i in range(n):
    # swapped = False
    for j in range(n - i- 1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1], arr[j]
            if swap_count == 1:
                break
            swap_count += 1
            # swapped = True 
            

            
    # if not swapped :
        # break
print(arr, swap_count)            


