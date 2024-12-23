def is_subset(arr1, arr2):
    arr1.sort()
    arr2.sort()

    i =0
    j = 0

    while i< len(arr1) and j < len(arr2):
        if arr1[i]  < arr2[j]:
            i += 1

        elif arr1[i] == arr2[j]:
            i += 1
            j += 1
        else:         
            return False
    return j == len(arr2)     
        

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

if is_subset(arr1, arr2):
    print("yes")
else: 
    print("no")