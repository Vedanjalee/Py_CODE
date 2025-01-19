from collections import deque 

def sliding_window_maximum(arr,k) :
    result = []

    dq = deque() 

    for i in range(len(arr)):

        if dq and dq[0] <i-k+1 :
            dq.popleft() 
        while dq and arr[dq[-1]] <arr[i] :
            dq.pop()
             
        dq.append(i) 

        if i>= k - 1 :
            result.append(arr[dq[0]])
    return result 

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_maximum(arr, k)
print(result)