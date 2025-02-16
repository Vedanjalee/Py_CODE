arr =[1,2,3,5]
n = len(arr) + 1
total = (n*(n+1))//2

all = sum(arr)
missing = total - all
print(missing)


