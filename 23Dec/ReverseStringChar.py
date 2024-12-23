str = "hello"
str = list(str)
l, r = 0 , len(str)-1 

while l<r:
    str[l] , str[r] = str[r], str[l]
    l += 1
    r -= 1
print(''.join(str))    

