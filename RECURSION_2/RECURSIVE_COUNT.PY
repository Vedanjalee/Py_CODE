def count_zeroes(n):
    if n==0:
        return 1 
    if n<10:
        return 0
    
    if n%10 == 0:
        return 1 + count_zeroes(n//10)
    else:
        return count_zeroes(n//10)
    
n = 1020030
print(count_zeroes(n))    