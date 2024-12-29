def Number(i,n):
    if (i>n):
        return 
    
    print(i)
    Number(i+1,n)

i = 1
n = 6
Ans = Number(i,n)
print(Ans)