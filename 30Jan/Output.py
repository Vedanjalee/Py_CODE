a = [1,2,3,4,5,6]

value = 3

# output = [1,2,3][4,5,6]
k = 2 
# [1,2][3,4][5,6]
i = 1 
j= 0
l =[]
out =[]

while (j<len(a) and i<=k):
    l += [a[j]]
    if(i==k):
        out += [l]
        l =[]
        i=0
    i+=1 
    j += 1    

print(out, "elements in paisr are equal to the K") 

