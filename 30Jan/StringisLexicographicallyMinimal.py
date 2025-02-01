def lexicographically_smallest_rotation(s):
   
    doubled = s + s  
    
    n = len(s) 
    smallest_rotation = doubled 

    for i in range(1, n):
        rotation = doubled[i:i + n]  
        
        
        if rotation < smallest_rotation:
            smallest_rotation = rotation  
    
    return smallest_rotation


s = "bca"
print("Smallest Lexicographical Rotation:", lexicographically_smallest_rotation(s))
