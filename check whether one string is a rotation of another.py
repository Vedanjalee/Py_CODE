def is_isomorphic(s1,s2):

    if len(s1) != len(s2):
        return False 
    
    s1_double = s1+s2

    return s2 in s1_double 

s1 = "waterbottle"
s2 = "erbottlewat"
result = is_isomorphic(s1, s2)
print(s2 ," a isomorphic of ",s1 , result)

s1 = "abc"
s2 = "bca"
result = is_isomorphic(s1, s2)
print(s2," a isomorphic of ",s1, result)

s1 = "abc"
s2 = "acb"
result = is_isomorphic(s1, s2)
print(s2, " a isomorphic of ",s1 ,result)
