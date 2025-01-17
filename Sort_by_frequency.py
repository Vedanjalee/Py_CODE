def sort_by_frequency_manual(arr):
    
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    
    sorted_array = sorted(arr, key=lambda x: (-frequency[x], x))
    
    return sorted_array


arr = [4, 6, 2, 6, 1, 4, 4, 6]
result = sort_by_frequency_manual(arr)
print("Array sorted by frequency:", result)
