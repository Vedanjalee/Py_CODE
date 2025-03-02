def is_Check_if_a_String_is_Interleaving_of_Other_Two_Recursive(A,B,C, i=0, j=0, k=0):

    if k==len(C) and i==len(A) and j==len(B):
        return True 
    
    if k==len(C):
        return False 
    
    # curr char matche C or not 

    if i<len(A) and A[i] == C[k] :
        if is_Check_if_a_String_is_Interleaving_of_Other_Two_Recursive(A,B,C, i+1, j, k+1) :
            return True 

    if j<len(B) and B[j] == C[k] :
        if is_Check_if_a_String_is_Interleaving_of_Other_Two_Recursive(A,B,C, i, j+1, k+1):
            return True 

    return False   

A = "abc"
B = "def"
C = "adbcef"
print(is_Check_if_a_String_is_Interleaving_of_Other_Two_Recursive(A,B,C))
