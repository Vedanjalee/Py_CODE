def Shortest_Common_Supersequence(s1, s2,m,n):
    if m==0:
        return n
    if n == 0:
        return m
    
    if s1[m-1] == s2[n-1]:
        return 1 + Shortest_Common_Supersequence(s1,s2,m-1, n-1)
    
    return 1+min(Shortest_Common_Supersequence(s1,s2,m-1,n), 
                   Shortest_Common_Supersequence(s1,s2, m,n-1))

s1 = "AGGTAB"
s2 = "GXTXAYB"

print("SCS Length (Brute Force):", Shortest_Common_Supersequence(s1, s2, len(s1), len(s2)))  