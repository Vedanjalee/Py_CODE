A =[16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
result = []
maxright = A[-1]
result.append(maxright)
for i in range(len(A)-2, -1,-1):
    if A[i] > maxright:
        maxright = A[i] 
        result.append(maxright)
print(result)        
        
