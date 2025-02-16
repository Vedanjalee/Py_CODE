def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    total = 0  
    for num in range(2, n + 1): 
        if is_prime(num):  
            total += num  
    return total


n = 10
print(f"Sum of prime numbers between 1 and {n}: {sum_of_primes(n)}")