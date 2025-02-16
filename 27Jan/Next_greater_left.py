def next_greater_left(arr):
    n  = len(arr)
    result = [-1] * n
    stack = [] 

    for i in range(n):

        while stack and stack[-1] <= arr[i]:
            stack.pop() 

        if stack :
            result[i] = stack[-1] 

        stack.append(arr[i]) 
    return result 

arr= [4, 5, 2, 10, 8]
print("Next Greater Element to Left:", next_greater_left(arr))        

