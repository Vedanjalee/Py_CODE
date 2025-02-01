def lexicographically_largest_rotation(s):
    
    doubled = s + s 
    
    n = len(s)  
    largest_rotation = ""  
    
    
    for i in range(n):
        rotation = doubled[i:i + n]  
        
        if rotation > largest_rotation:
            largest_rotation = rotation  
    
    return largest_rotation

s = "bca"
print("Largest Lexicographical Rotation:", lexicographically_largest_rotation(s))
