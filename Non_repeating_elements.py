def non_repeating_elements(arr):
    freq = {} 

    for num in arr :
        if num in freq :
            freq[num] += 1 
        else:
            freq[num] = 1

    non_repeating = [key for key , value in freq.items() if value == 1   ]    
    return non_repeating        

arr = [4,5,4,5 ,6,7,8,6]

non_repeating = non_repeating_elements(arr)

print("Non-repeating elements are:", non_repeating)