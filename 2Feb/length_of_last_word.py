def length_of_last_word(A):

    n = len(A)
    count = 0 
    i = n-1 

    while i>=0 and A[i] == ' ' :
        i -= 1


    while i>=0 and A[i] != ' ' :
        count += 1
        i -= 1
    return count      

A = " hello world "
print(length_of_last_word(A))  # Output: 5


A = "InterviewBit"
print(length_of_last_word(A))  # Output: 12  