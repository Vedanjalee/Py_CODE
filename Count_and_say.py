def countAndSay(n):
    # Base cases
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    # Initialize the first term
    s = "11"  # This is the 2nd term (as base)

    # Generate terms from 3 to n
    for i in range(3, n + 1):
        cnt = 1  # Initialize the count of matching characters
        tmp = ""  # Initialize the next term in the sequence

        # Process the previous term (s) to find the next term
        for j in range(1, len(s)):
            # If the current character doesn't match the previous one
            if s[j] != s[j - 1]:
                # Append the count and the character to the result string
                tmp += str(cnt) + s[j - 1]
                # Reset the count
                cnt = 1
            else:
                # If they match, increment the count
                cnt += 1

        # Append the last group (the last sequence of characters)
        tmp += str(cnt) + s[-1]
        
        # Update s for the next iteration
        s = tmp

    return s

# Driver Code
N = 2111
print(countAndSay(N))  # Output: "21"
