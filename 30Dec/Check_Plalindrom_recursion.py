def pallindrome(s,i):
    n = len(s)

    if i>= n//2 :
        return True
    if s[i] != s[n-i-1]:
        return False
    
    return pallindrome(s, i+1)

s= "radar"
result = pallindrome(s,0)

print(result)
