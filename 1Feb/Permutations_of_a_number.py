def permutations(s, left, right):

    if left == right : 
        print("".join(s))
    else :
        for i in range(left, right + 1):

            s[left], s[i] = s[i] , s[left] 

            permutations( s, left+1 , right) 

            s[left] , s[i] = s[i] , s[left] 

s = input("enter a string   :")
n = len(s)


permutations(list(s), 0, n-1)
