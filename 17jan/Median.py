def median_of_array(arr):
    arr.sort() 

    n = len(arr)

    if n%2 == 1:
        median = arr[n//2]

    else:
        median =int((arr[n//2 - 1] + arr[n//2]) / 2  ) 
    return median 

arr = [3, 1,6, 7, 5, 4]
median = median_of_array(arr)
print("Median of", arr, "is:", median)
    