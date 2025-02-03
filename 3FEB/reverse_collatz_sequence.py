def reverse_collatz_sequence(n):
    sequence = [1]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence[::-1]

n = 5
print(f"Reverse Collatz sequence for {n}: {reverse_collatz_sequence(n)}")
