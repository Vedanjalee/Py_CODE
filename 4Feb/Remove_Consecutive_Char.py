def remove_consecutive_char(A,B):

    while True:
        found = False 
        i = 0
        n = len(A)
        result =[]

        while i<n  :
            count = 1
            while i +count < n and A[i] == A[i+ count]:
                count += 1


            if count == B:
                found = True 
                i += B 

            else:
                result.append(A[i])
                i += 1
        A = ''.join(result)
        
        if not found:
            break
            
    return A       

A = input("Enter the string: ")
B = int(input("Enter the integer B (length of consecutive characters to remove): "))


result = remove_consecutive_char(A, B)
print("Result after removals:", result) 



