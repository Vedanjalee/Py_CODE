def pick_from_both_sides(A, B):
    n = len(A)
    
    # Step 1: Calculate prefix sums
    prefix_sum = [0] * (n + 1)  # To store sums from the start
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]

    # Step 2: Calculate suffix sums
    suffix_sum = [0] * (n + 1)  # To store sums from the end
    for i in range(n - 1, -1, -1):
        suffix_sum[n - i] = suffix_sum[n - i - 1] + A[i]

    # Step 3: Try all combinations of picking k elements from the start
    # and B - k elements from the end
    max_sum = float('-inf')
    for k in range(B + 1):
        left_sum = prefix_sum[k]  # Sum of first k elements
        right_sum = suffix_sum[B - k]  # Sum of last B - k elements
        max_sum = max(max_sum, left_sum + right_sum)

    return max_sum

# Example Usage
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = 3
print("Maximum sum of picked elements:", pick_from_both_sides(A, B))
