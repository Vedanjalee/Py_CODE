def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot =arr[-1]

    left  = []
    right =[]
    for x in arr[:-1]:
        if x<= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)        

    
arr = [38, 27, 43, 3, 9, 82, 10]
print("sorted array", quick_sort(arr))        
