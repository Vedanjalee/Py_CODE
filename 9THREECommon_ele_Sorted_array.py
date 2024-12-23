A = [1, 5, 10, 20, 30]
B = [1,5, 13, 15, 20]
C = [1,5, 20]
# Common Elements: 1 5 20 


i,j,k =0,0,0

common =[]

while i<len(A) and j<len(B) and k<len(C):
    if A[i] == B[j] and B[j] == C[k]:
        common.append(A[i])
        i += 1
        j += 1
        k += 1

        while i<len(A) and A[i] == A[i-1]:
            i += 1
        while j<len(B) and B[i] == B[i-1]:     
            j += 1
        while k< len(C) and C[k] == C[k-1]:
            k += 1

    elif A[i] < B[j]:
        i += 1

    elif B[j] < C[k]:
        j += 1
    else: 
        k += 1
print(common)                        



