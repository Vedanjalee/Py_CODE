def nearest_snaller_left(arr) :
    n = len(arr)
    stack = []
    result = [-1] * n 

    for i in range(n) : 
        while stack and stack[-1] > arr[i ] :
            stack.pop() 

        if stack:
            result[i] = stack[-1] 

        stack.append(arr[i]) 
    return result 

arr = [4, 5, 2, 10, 8]
print("next smaller ele ......", nearest_snaller_left(arr))     ;

