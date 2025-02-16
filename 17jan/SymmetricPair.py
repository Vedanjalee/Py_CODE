def find_symmetric_pairs(pairs):
    
    pair_map = {}
    symmetric_pairs = []  
   
    for a, b in pairs:
        
        if b in pair_map and pair_map[b] == a:
           
            symmetric_pairs.append((a, b))
        else:
           
            pair_map[a] = b

    return symmetric_pairs


pairs = [(1, 2), (3, 5), (2, 1), (5, 3), (4, 7)]
result = find_symmetric_pairs(pairs)
print("Symmetric pairs are:", result)
