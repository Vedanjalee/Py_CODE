def rotate( arr):
        # temp = arr[-1]
        # for i in range(len(arr)-2,-1,-1):
        #     arr[i+1] = arr[i]
        # arr[0] = temp    
        # return arr   

        temp = arr[0]
        for i in range(1,len(arr)):
            arr[i-1] = arr[i]
        arr[-1] = temp    
        return arr   
arr = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
print(rotate(arr)) 
            