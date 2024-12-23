def isSortedOrRotated(A):
    count_br = 0 
    for i in range(1,len(A)):
        if A[i-1] > A[i]:
            count_br += 1

    if count_br == 0:
        return("arrray sorted")   
    else: 
        return("array not sorted")         


A =[1,2,3,4]

# A =[5, 4, 3, 2, 1]
print(isSortedOrRotated(A))  