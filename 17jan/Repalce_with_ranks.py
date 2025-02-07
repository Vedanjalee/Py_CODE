def replace_with_ranks(arr):
   
    sorted_unique = sorted(set(arr))
    
    rank_map = {}
    rank = 1  
    for value in sorted_unique:
        rank_map[value] = rank
        rank += 1
    

    ranked_array = []
    for element in arr:
        ranked_array.append(rank_map[element])
    
    return ranked_array


arr = [40, 10, 20, 30]
result = replace_with_ranks(arr)
print("Array after replacing elements with ranks:", result)
