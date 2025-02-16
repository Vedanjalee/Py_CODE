def all_circular_rotations(s):
    rotations =[]
    n = len(s)
    
    
    for i in range(n):
        rotation = s[i:] + s[:i]
        rotations.append(rotation)
    return rotations

s = "abc"
print("All Circular Rotations:", all_circular_rotations(s))
