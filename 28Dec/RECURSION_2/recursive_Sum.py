def findSum(n):
    if n==0:
        return 0
    return n + findSum(n-1)

n = 5
print(findSum(n))