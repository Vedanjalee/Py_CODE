A=[2,3,4,57,8,1,2,3]
for i in range(len(A)):
    min_idx = i

    for j in range(i+1, len(A)):
        if A[j]<A[min_idx]:
            min_idx = j

            A[min_idx],A[i] = A[i], A[min_idx]
print(A)            