def majority_ele(arr):
    candidate = None 
    count  = 0 

    for num in arr:
        if count == 0 :
            candidate = num 
        count += 1     