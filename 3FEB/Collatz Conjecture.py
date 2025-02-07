# The Collatz Conjecture, also known as the "3n + 1 problem," is a famous unsolved problem in mathematics. It states that for any positive integer n, if you repeatedly apply the following rules, you will eventually reach 1:

# If n is even, divide it by 2:
# 𝑛
# =
# 𝑛
# /
# 2
# n=n/2
# If n is odd, multiply it by 3 and add 1:
# 𝑛
# =
# 3
# 𝑛
# +
# 1
# n=3n+1

n = 5 
# ans = [5,16,8,4,2,1] 
numbers =[] 
while n != 1:
    numbers.append(n)
    if (n%2 == 0 ):
        n = n//2 

    else : 
        n = n*3 + 1 

numbers.append(1)        

print("Collatz sequence:", numbers)