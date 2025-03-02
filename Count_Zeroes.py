def count_zeros(n):
    count = 0
    while n>0 :
        if n%10 == 0:
            count += 1
        n //= 10
    return count 

num = 1020304050
print(count_zeros(num))