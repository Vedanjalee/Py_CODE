def func(n):
    if n==0:
        return 0
    return n + func(n-1)   

n = 3
new = func(n)
print(new, "Sum of N numbers ") 