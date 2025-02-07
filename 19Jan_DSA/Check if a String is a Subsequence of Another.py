from collections import deque

def is_subsequence(s, t):
    dq = deque(s) 
    for char in t :
        if not dq :
            break 

        if char==dq[0]:
            dq.popleft() 
    return not dq 

s = "abc"
t = "ahbgdc"
result = is_subsequence(s, t)
print(result)