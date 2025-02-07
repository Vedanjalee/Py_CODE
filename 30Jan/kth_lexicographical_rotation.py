def kth_lexicographical_rotation(s, k):
    n = len(s)
    rotations = []
    for i in range(n):
        rotation = s[i:] + s[:i]  
        rotations.append(rotation)  

    rotations.sort()

    if k <= n:
        return rotations[k - 1]  
    else:
        return "Invalid input" 
    
s = "abcde"
k = 2
print(f"{k}th Lexicographical Rotation:", kth_lexicographical_rotation(s, k))
