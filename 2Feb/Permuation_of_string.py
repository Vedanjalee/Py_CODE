def Permutaion_of_string(s, l, r):

    if l == r :
        print("".join(s))

    else:

        for i in range(l, r + 1):
            s[l], s[i] = s[i] , s[l] 

            Permutaion_of_string(s, l+1, r)
            s[l], s[i] = s[i] , s[l] 

s = list("ABC")
Permutaion_of_string(s,0, len(s)-1)
