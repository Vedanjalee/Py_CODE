A = [20, 211, 45, 89, 89, 90]

is_sorted = True
for i in range(1,len(A)):
    if (A[i-1] > A[i]):
        is_sorted= False
   
if is_sorted: 
    print("sorted")

else: 
    print("not sorted")   



# new = sorted(A)
# if A == new:
#     print("sorted")
# else:
#     print("not sorted")    